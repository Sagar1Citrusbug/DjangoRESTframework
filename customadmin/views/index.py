from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from Custom.models import book, Author, transaction
from django.shortcuts import render


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "customadmin/index.html"
    context = {}

    def get(self, request):
        self.context['review_categories'] = book.objects.all().count()
        self.context['review_brands'] = Author.objects.all().count()
        self.context['reviews'] = transaction.objects.all().count()
        return render(request, self.template_name, self.context)
