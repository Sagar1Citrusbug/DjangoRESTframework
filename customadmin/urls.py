from django.urls import path
from customadmin import views 
from django.contrib.auth import views as auth_views
# from Custom import views
app_name  = "customadmin"

urlpatterns = [
    path("",views.Login.as_view() , name  = "cust_admin_login" )
    
]
