
from turtle import title
from Custom.models import  transaction
from customadmin.views.generic import MyCreateView, MyDeleteView, MyListView, MyUpdateView, MyLoginRequiredView
# from django.views import View
from django.db.models import Q
from django.template.loader import get_template
from django_datatables_too.mixins import DataTableMixin
from django.urls import reverse
from django.http import JsonResponse
from customadmin.forms import TransactionCreateForm, TransactionUpdateForm


from customadmin.mixins import HasPermissionsMixin

class TransactionListView(MyListView):
    ordering = ["-id"]
    model = transaction
    queryset = model.objects.all()
    template_name = "customadmin/Transaction/Transaction_list.html"
    permission_required = ("Custom.view_Transaction",)
class TransactionCreateView(MyCreateView):
    model = transaction
    form_class = TransactionCreateForm
    template_name = "customadmin/transaction/transaction_update.html"
    permission_required = ("Custom.add_transaction",)

    def form_valid(self, form):
        form.instance.create_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # opts = self.model._meta
        return reverse("customadmin:transaction-list")
class TransactionUpdateView(MyUpdateView):
    model = transaction
    form_class = TransactionUpdateForm
   
    template_name = "customadmin/transaction/transaction_update.html"
    permission_required = ("Custom.change_transaction",)

    def get_success_url(self):
      
        return reverse("customadmin:transaction-list")


class TransactionDeleteView(MyDeleteView):
    model = transaction
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("Custom.delete_transaction",)

    def get_success_url(self):
       
        return reverse("customadmin:transaction-list")

class TransactionAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """
    Ajax-Pagination view for ReviewCategory
    """
    model = transaction
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
        t = get_template("customadmin/transaction/transaction_actions.html")
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
                Q(issue_date__icontains=self.search)|
                Q(return_date__icontains=self.search)
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
            # url = reverse("customadmin:Transaction-list", kwargs={'pk': o.pk})
            data.append(
                {
                    "id": o.id,
                    # "name":  "<a href='" + url + "'>" + o.name + "</a>",
                    "user": o.user.name,
                    "books":o.books.title,
                    "issue_date":o.issue_date,
                     "return_date":o.return_date,
                    
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
