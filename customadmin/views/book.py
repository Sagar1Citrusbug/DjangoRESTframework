from Custom.models import book, myUser, Author
from customadmin.views.generic import MyCreateView, MyDeleteView, MyListView, MyUpdateView
from django.views import View
from django.urls import reverse
from customadmin.forms import BookCreateForm, BookUpdateForm


class BookList(MyListView):
    ordering = ["-id"]
    model = book
    queryset = model.objects.all()
    template_name = "customadmin/review_category/review_category_list.html"
    permission_required = ("custom.view_book",)


class BookCreateView(MyCreateView):
    model = book
    form_class = BookCreateForm
    template_name = "customadmin/review_category/review_category_form.html"
    permission_required = ("Custom.add_book",)

    def form_valid(self, form):
        form.instance.create_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # opts = self.model._meta
        return reverse("customadmin:book-list")
class BookUpdateView(MyUpdateView):
    model = book
    form_class = BookUpdateForm
    template_name = "customadmin/review_category/review_category_form.html"
    permission_required = ("Custom.change_book",)

    def get_success_url(self):
        print("''''''''''''''reverse'''''''''''''''")
        return reverse("customadmin:book-list")

class BookDeleteView(MyDeleteView):
    model = book
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("Custom.delete_book",)

    def get_success_url(self):
        return reverse("customadmin:book-list")