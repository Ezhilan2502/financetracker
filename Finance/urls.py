from django.urls import path
from . import views

urlpatterns=[
    path('',views.base,name='base'),
    path('message_redirect/',views.message_redirect,name='message_redirect'),
    path('register/',views.register,name='register'),
    path('verify_otp/',views.verify_otp,name='verify_otp'),
    path('login/',views.login,name='login'),
    path('monthly_export',views.monthly_export,name='monthly_export'),
    path('forget_password/',views.forget_password,name='forget_password'),
    path('verify_otp1/',views.verify_otp1,name='verify_otp1'),
    path('logout_view/',views.logout_view,name='logout_view'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('list/',views.transaction_list,name='transaction_list'),
    path('add/',views.add_transaction,name='add_transaction'),
    path('transactions/edit/<int:pk>/', views.edit_transaction, name='edit_transaction'),
    path('transactions/delete/<int:pk>/', views.delete_transaction, name='delete_transaction'),
    path('list1/',views.goal_list,name='goal_list'),
    path('add1/',views.add_goal,name='add_goal'),
    path('contribute_to_goal/<int:pk>',views.contribute_to_goal,name='contribute_to_goal'),
    path('goals1/edit/<int:pk>/', views.edit_goal, name='edit_goal'),
    path('goals1/delete/<int:pk>/', views.delete_goal, name='delete_goal')
]
