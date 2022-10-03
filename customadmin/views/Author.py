from Custom.models import book, myUser, Author
from customadmin.views.generic import MyCreateView, MyDeleteView, MyListView, MyUpdateView
from django.views import View
class AuthorListView(MyListView):
    pass
class AuthorCreateView(MyCreateView):
    pass
class AuthorUpdateView(MyUpdateView):
    pass
class AuthorDeleteView(MyDeleteView):
    pass