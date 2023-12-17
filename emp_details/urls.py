from django.urls import path
from emp_details import views

urlpatterns = [
    path("",views.home,name="system check"),
    path('success/',views.success,name="Success"),
    path("add/",views.add_employee,name="add_employee"),
    path("all_emp/",views.all_emp_data,name='all_emp_data'),
    path("update/<id>",views.update_emp,name='update_emp_data'),
    path("delete/",views.delete_emp,name='delete_emp_data'),
    path("delete_employee/",views.delete_employee,name='delete_employee'),
    
]
