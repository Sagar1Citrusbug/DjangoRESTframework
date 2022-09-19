from django.urls import path
from . import views
app_name = 'Custom'
urlpatterns = [
    path("allusers/", views.UserListView.as_view(), name = "UserListView"),
    path("allusers/<int:pk>", views.UserDetailView.as_view(), name = "UserDetailView"),
    path("excluded/", views.apibymixin.as_view(), name = "mixinapi"),
    path("author/", views.authorlist.as_view(), name = "authorapi"),
    path("books/", views.booklist.as_view(), name  = "bookapi"),
    path("bookuser/<int:pk>", views.bookuser.as_view(), name = "bookuserapi"),
    path("transaction/", views.trans.as_view(), name = "transaction")
]
