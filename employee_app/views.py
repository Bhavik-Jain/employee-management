# from django.shortcuts import render, HttpResponse
# from .models import Employee, Department, Role
# # Create your views here.

# def index(request):
#     return render(request, 'index.html')


# def view_emp(request):
#     employees = Employee.objects.all()
#     context = {
#         'emps': employees
#     }

#     print(context)
#     return render(request, 'view_emp.html', context)


# def add_emp(request):
#     if request.method == "POST":
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         dept_name = request.POST['dept']  # Get department name from the form
#         salary = int(request.POST['salary'])
#         bonus = int(request.POST['bonus'])
#         role_name = request.POST['role']  # Get role name from the form

#         # Retrieve department and role objects based on their names
#         dept = Department.objects.get(name=dept_name)
#         role = Role.objects.get(name=role_name)

#         # Create and save the Employee object with department and role IDs
#         emp = Employee(first_name=first_name, last_name=last_name, dept=dept, salary=salary, role=role, bonus=bonus)
#         emp.save()
#         return HttpResponse('Employee Added Successfully')
#     elif request.method == "GET":
#         return render(request, 'add_emp.html')
#     else:
#         return HttpResponse('An Error Occurred')

# def remove_emp(request,emp_id=0):
#     if emp_id:
#         try:
#             emp_to_be_removed = Employee.objects.get(id=emp_id)
#             emp_to_be_removed.delete()
#             return HttpResponse('Employee removed successfully')
#         except:
#             return HttpResponse('Please enter a valid employee')
#     employees = Employee.objects.all()
#     context = {
#         'emps': employees
#     }
#     return render(request, 'remove_emp.html', context)


from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Employee, Department, Role
from .serializers import EmployeeSerializer
from django.shortcuts import render,redirect
from .pagination import Pagination

@api_view(['GET'])
def index(request):
    return render(request, 'index.html')

class EmployeeListView(APIView):
    pagination_class = Pagination
    def get(self, request):
        employees = Employee.objects.all()
        paginator = self.pagination_class()

        # Enable when using Paginator
        # result_page = paginator.paginate_queryset(employees, request) 
        # serializer = EmployeeSerializer(result_page, many=True)

        serializer = EmployeeSerializer(employees, many=True)
        return render(request, 'view_emp.html', {'emps': serializer.data})
        # return render(request, 'view_emp.html', {'emps': serializer.data, 'paginator': paginator})

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class AddEmployeeView(APIView):
    def post(self, request):
        try:
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            dept_name = request.data.get('dept')
            salary = int(request.data.get('salary'))
            bonus = int(request.data.get('bonus'))
            role_name = request.data.get('role')

            dept = Department.objects.get(name=dept_name)
            role = Role.objects.get(name=role_name)

            emp = Employee(first_name=first_name, last_name=last_name, dept=dept, salary=salary, role=role, bonus=bonus)
            emp.save()

            return redirect('employee-list')
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=400)

    def get(self, request):
        return render(request, 'add_emp.html')


class EmployeeDeleteView(APIView):
    def get(self, request):
        try:
            employees = Employee.objects.all()
            context = {
                'emps': employees
            }
            return render(request, 'remove_emp.html', context)
        except:
            return render(request, 'Page Not Found')

class EmployeeDetailView(APIView):
    def get(self, request, emp_id):
        if emp_id:
            try:
                emp_to_be_removed = Employee.objects.get(id=emp_id)
                emp_to_be_removed.delete()
                return redirect('remove-employee')
            except:
                return HttpResponse('Please enter a valid employee')

    def delete(self, request, emp_id):
        emp = self.get_object(emp_id)
        if emp:
            emp.is_active = False
            emp.save()
            return HttpResponse('Employee removed successfully')
        return HttpResponse('Please enter a valid employee')

    def get_object(self, emp_id):
        try:
            return Employee.objects.get(id=emp_id)
        except Employee.DoesNotExist:
            return None

# class DepartmentListView(APIView):
#     def get(self, request):
#         departments = Department.objects.all()
#         serializer = DepartmentSerializer(departments, many=True)
#         return JsonResponse(serializer.data, safe=False)

# class RoleListView(APIView):
#     def get(self, request):
#         roles = Role.objects.all()
#         serializer = RoleSerializer(roles, many=True)
#         return JsonResponse(serializer.data, safe=False)
