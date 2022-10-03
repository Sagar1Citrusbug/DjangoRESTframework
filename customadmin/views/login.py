# import imp
from Custom.forms import LogPage
from Custom.models import myUser
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views import View
from Custom.models import book, Author, transaction, myUser


class Login(View):
    
    def get(self,request):
        context = {}
        form = LogPage()
        context['form']  = form
        return render(request,"Custom/login.html", context)
    def post(self,request):


        context= {}
        context['review_categories'] = book.objects.all().count()
        context['review_brands'] = Author.objects.all().count()
        context['reviews'] = transaction.objects.all().count()
        if request.method  == 'POST':
               
            form = LogPage(request.POST)
            context['form'] = form
       
            if form.is_valid():
       
                email =  form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = myUser.objects.filter(email = email).first()
           
                if user:

       
                   account = authenticate(email = email, password = password)
                    
                   if account:
                       if account.has_perm("is_admin", account):
                        login(request, user)
                        redirect('/index')
                        return render(request,"customadmin/index.html", context)

                   else:
                        return HttpResponse("password or email is wrong")
                else:
                    return  HttpResponse("NO user exists")
           
            else:
           
                return render(request, "customadmin/ebr/registration/login.html",{'form':form} )