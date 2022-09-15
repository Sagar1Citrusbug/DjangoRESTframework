from django.urls import path
from . import views
app_name = 'Custom'
urlpatterns = [
    path("allusers/", views.UserListView.as_view(), name = "UserListView"),
    path("allusers/<int:pk>", views.UserDetailView.as_view(), name = "UserDetailView"),
    path("excluded/", views.apibymixin.as_view(), name = "mixinapi")
]
