
from Custom.models import  Author
from customadmin.views.generic import MyCreateView, MyDeleteView, MyListView, MyUpdateView, MyLoginRequiredView
# from django.views import View
from django.db.models import Q
from django.template.loader import get_template
from django_datatables_too.mixins import DataTableMixin
from django.urls import reverse
from django.http import JsonResponse


from customadmin.mixins import HasPermissionsMixin

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


class AuthorAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """
    Ajax-Pagination view for ReviewCategory
    """
    model = Author
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
        t = get_template("customadmin/partials/list_row_actions.html")
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
                Q(name__icontains=self.search) |
                Q(email__icontains=self.search)
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
                    "name": o.name,
                    "email":o.email,
                    
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
