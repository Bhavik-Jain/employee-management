# from django.urls import path
# from . import views


# urlpatterns = [
#     path('', views.index, name = 'index'),
#     path('view_emp', views.view_emp, name = 'view_emp'),
#     path('add_emp', views.add_emp, name = 'add_emp'),
#     path('remove_emp', views.remove_emp, name = 'remove_emp'),
#     path('remove_emp/<int:emp_id>', views.remove_emp, name = 'remove_emp'),
# ]

from django.urls import path
from .views import index, EmployeeListView, EmployeeDetailView, AddEmployeeView, EmployeeDeleteView

urlpatterns = [
    path('', index, name='index'),
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:emp_id>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('remove_emp', EmployeeDeleteView.as_view(), name='remove-employee'),
    path('add_emp/', AddEmployeeView.as_view(), name='add-employee'),
]