from Custom.models import book
from customadmin.views.generic import MyCreateView, MyDeleteView, MyListView, MyUpdateView, MyLoginRequiredView
from django.urls import reverse
from customadmin.forms import BookCreateForm, BookUpdateForm

from customadmin.mixins import HasPermissionsMixin
from django.db.models import Q
from django.template.loader import get_template
from django_datatables_too.mixins import DataTableMixin
from django.urls import reverse
from django.http import JsonResponse


class BookList(MyListView):
    ordering = ["-id"]
    model = book
    queryset = model.objects.all()
    template_name = "customadmin/book/book_list.html"
    permission_required = ("Custom.view_book",)


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
      
        return reverse("customadmin:book-list")

class BookDeleteView(MyDeleteView):
    model = book
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("Custom.delete_book",)

    def get_success_url(self):
        print("------------inside delsucurl_-----------------------")
        return reverse("customadmin:book-list")


class BookAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """
    Ajax-Pagination view for ReviewCategory
    """
    model = book
    queryset = model.objects.all().order_by("-id")

    def _get_is_superuser(self, obj):
        """Get boolean column markup."""
        t = get_template("customadmin/partials/list_boolean.html")
        return t.render({"bool_val": obj.is_superuser})

    def is_orderable(self):
        """Check if order is defined in dictionary."""
        # if self._querydict.get("order"):
        #     return True
        return True

    def _get_actions(self, obj):
        """Get actions column markup."""
        t = get_template("customadmin/book/book_actions.html")
        opts = self.model._meta
        return t.render({
            "o": obj,
            "opts": opts,
            "has_change_permission": self.has_change_permission(self.request),
            "has_delete_permission": self.has_delete_permission(self.request),
        })

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            return qs.filter(
                Q(title__icontains=self.search) |
                Q(category__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        """Prepare final result data here."""
        # Create row data for datatables
        data = []
        for o in qs:
        #     if o.slug:
        #         slug = o.slug
        #     else:
        #         slug = '-'
            # url = reverse("customadmin:author-list", kwargs={'pk': o.pk})
            data.append(
                {
                    "id": o.id,
                    # "name":  "<a href='" + url + "'>" + o.name + "</a>",
                    "title": o.title,
                    "author":o.author.name,
                    "category":o.category,
                    "actions": self._get_actions(o),
                }
            )
        return data

    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        total_filter_data = len(self.filter_queryset(self.model.objects.all().order_by("-id")))
        context_data['recordsTotal'] = len(self.model.objects.all().order_by("-id"))
        context_data['recordsFiltered'] = total_filter_data
        return JsonResponse(context_data)