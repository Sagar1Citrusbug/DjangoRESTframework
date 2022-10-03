from django import forms
from Custom.models import book, Author, transaction
from django.forms import ModelForm


class BookCreateForm(ModelForm):
    class Meta:
        model = book
        fields = '__all__'

class AuthorCreateForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']

class BookUpdateForm(ModelForm):

    class Meta:
        model = book
        fields = '__all__'

class AuthorUpdateForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']