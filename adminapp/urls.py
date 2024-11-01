from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.projecthomepage, name='projecthomepage'),
    path('printpagecall/', views.printpagecall, name='printpagecall'),
    path('printpagelogic/', views.printpagelogic, name='printpagelogic'),
    path('exceptionpagecall/', views.exceptionpagecall, name='exceptionpagecall'),
    path('exceptionpagelogic/', views.exceptionpagelogic, name='exceptionpagelogic'),
    path('randompagecall/', views.randompagecall, name='randompagecall'),
    path('randomlogic/', views.randomlogic, name='randomlogic'),
    path('calculatorpagecall/', views.calculatorpagecall, name='calculatorpagecall'),
    path('calculatorlogic/', views.calculatorlogic, name='calculatorlogic'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('datetimepagecall/', views.datetimepagecall, name='datetimepagecall'),
    path('datetimepagelogic/', views.datetimepagelogic, name='datetimepagelogic'),
    path('UserRegisterPageCall/',views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('UserRegisterLogic/',views.UserRegisterLogic, name='UserRegisterLogic'),
    path('UserLoginPageCall/',views.UserLoginPageCall, name='UserLoginPageCall'),
    path('UserLoginLogic/',views.UserLoginLogic, name='UserLoginLogic'),
    path('logout/',views.logout, name='logout'),
    path('add_student',views.add_student,name='add_student'),
    path('student_list',views.student_list,name='student_list'),
    path('upload_file',views.upload_file,name='upload_file'),
    path('feedBack',views.feedBack,name='feedBack'),
    path('con_man/', views.con_man, name='con_man'),
    path('<int:pk>/del/', views.del_con_man, name='del_con_man'),
]