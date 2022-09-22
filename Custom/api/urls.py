from django.urls import path
from . import views
app_name = 'Custom'
urlpatterns = [
    path("user/", views.UserListView.as_view(), name = "UserListView"),
    path("user/<int:pk>", views.UserDetailView.as_view(), name = "UserDetailView"),
    path("author/", views.bookauthorlist.as_view(), name = "bookauthorlistapi"),
    path("author/<int:pk>", views.bookauthor.as_view(), name = "bookauthorapi"),
    path("book/", views.bookuserlist.as_view(), name = "bookuserlistapi"),
    path("book/<int:pk>", views.bookuser.as_view(), name = "bookuserapi"),
    path("transaction/", views.trans.as_view(), name = "transaction")
]
