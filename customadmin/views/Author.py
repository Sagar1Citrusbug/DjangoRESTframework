from Custom.models import book, myUser, Author
from customadmin.views.generic import MyCreateView, MyDeleteView, MyListView, MyUpdateView
from django.views import View
class AuthorListView(MyListView):
    ordering = ["-id"]
    model = Author
    queryset = model.objects.all()
    template_name = "customadmin/author/author_list.html"
    permission_required = ("Custom.view_Author",)
class AuthorCreateView(MyCreateView):
    pass
class AuthorUpdateView(MyUpdateView):
    pass
class AuthorDeleteView(MyDeleteView):
    pass