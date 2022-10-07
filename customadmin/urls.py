from django.urls import path
from customadmin import views
from django.contrib.auth import views as auth_views
from Custom.api import views as api_views
# from customadmin.views.Author import AuthorAjaxPagination


app_name  = "customadmin"

urlpatterns = [
    path("",views.Login.as_view() , name  = "cust_admin_login" ),
    path("index/", views.IndexView.as_view(), name = "index"),
    path("book-list/",views.BookList.as_view(), name = "book-list"),
    path('author-list/',views.AuthorListView.as_view(),name='author-list'),
    path('transaction-list/',views.TransactionListView.as_view(),name='transaction-list'),
    path('book-change/<int:pk>', views.BookUpdateView.as_view(),name='book-update'),
    path('author-change/<int:pk>',views.AuthorUpdateView.as_view(),name='author-update'),
    path('transaction-change/<int:pk>',views.TransactionUpdateView.as_view(),name='transaction-update'),
    path('book-delete/<int:pk>',views.BookDeleteView.as_view(),name='book-delete'),
    path('author-delete/<int:pk>',views.AuthorDeleteView.as_view(),name='author-delete'),
    path('transaction-delete/<int:pk>',views.TransactionDeleteView.as_view(),name='transaction-delete'),
    path('book-create/',views.BookCreateView.as_view(),name='book-create'),
    path('author-create/',views.AuthorCreateView.as_view(),name='author-create'),
    path('transaction-create/',views.TransactionCreateView.as_view(),name='transaction-create'),
    path('ajax-author', views.AuthorAjaxPagination.as_view(), name = "author-list-ajax"),
    path('ajax-book', views.BookAjaxPagination.as_view(), name = "book-list-ajax"),
    path('ajax-transaction', views.TransactionAjaxPagination.as_view(), name = "transaction-list-ajax"),
    path('logout/',views.logout.as_view(), name = "logout")
    
	# path("ajax-agency-user", AgencyUserAjaxPagination.as_view(), name="agencyuser-list-ajax"),
]
    

