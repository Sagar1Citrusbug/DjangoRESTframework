from django.urls import path
from customadmin import views
from django.contrib.auth import views as auth_views
from Custom.api import views as api_views

app_name  = "customadmin"

urlpatterns = [
    path("",views.Login.as_view() , name  = "cust_admin_login" ),
    path("index/", views.IndexView.as_view(), name = "index"),
    path("book-list/",views.BookList.as_view(), name = "book-list"),
    path('auhtor-list/',views.AuthorListView.as_view(),name='author-list'),
    path('book-change/<int:pk>', views.BookUpdateView.as_view(),name='book-update'),
    path('author-change/<int:pk>',views.AuthorUpdateView.as_view(),name='author-update'),
    path('book-delete/<int:pk>',views.BookDeleteView.as_view(),name='book-delete'),
    path('client-delete/<int:pk>',views.AuthorDeleteView.as_view(),name='Author-delete'),
    path('book-create/',views.BookCreateView.as_view(),name='book-create'),
    path('author-create/',views.AuthorCreateView.as_view(),name='author-create')
	# path("ajax-agency-user", AgencyUserAjaxPagination.as_view(), name="agencyuser-list-ajax"),
]
    

