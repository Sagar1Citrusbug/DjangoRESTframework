from django.contrib import admin
 
from .models import myUser, book, Author, transaction



admin.site.register(myUser)
admin.site.register(book)
admin.site.register(Author)
admin.site.register(transaction)
