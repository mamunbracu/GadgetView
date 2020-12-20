from django.urls import path
from App_Complain import views

app_name = 'App_Complain'

urlpatterns = [
    path('complain/', views.complain, name='complain'),
]