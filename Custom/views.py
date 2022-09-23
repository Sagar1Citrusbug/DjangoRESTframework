from rest_framework import status

from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from .models import myUser

from .forms import Register, LogPage, passwordchangeform,forgetpass, Reset
from .api.serializers import Userserializer

from rest_framework.renderers import  JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response


def thanks(request):
    return render(request, "Custom/thanks.html")
def home(request):
   
    context  ={}
   
    return render(request, "Custom/all_users.html", context)




def registration_view(request):
    context = {}
    if request.method == 'POST':
        
        form = Register(request.POST)
        
        if form.is_valid():
           
            
            form.save()
            
            email =  form.cleaned_data.get('email')
            name   = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password1')
           

            return redirect("thanks")
        else:
           
            context['form'] = form
            return render(request, "Custom/register.html", context)

    else:
       
        form= Register()
        context['form'] = form
        return render(request, "Custom/register.html", context)

def forgetpassword(request):
   
    if request.method == 'POST':
        
        form = forgetpass(request.POST)
        if form.is_valid():
          email  = form.cleaned_data.get('email') 
          if myUser.objects.filter(email=email).exists():
            recent_user = myUser.objects.get(email = email)
            id = recent_user.id
            context = {
                "user":recent_user,
            }
            return redirect("Resset", pk = id)
           
          else:
            return HttpResponse("NO User exist, please register first")
        else:
            form  = forgetpass(request.POST)
            return render(request, "Custom/forgetpass.html") 
    else:
        form  = forgetpass()
        return render(request,"Custom/forgetpass.html",{'form':form})
def reset(request,pk):
    
   
    if request.method == 'POST':

        form = Reset(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user  = myUser.objects.get(id = pk)
            user.set_password(new_password)
            user.save()

            return HttpResponse("password has been reset")
        else:

            form = Reset(request.POST)
            return render(request, "Custom/reset.html",{'form':form})  
    else:
        form = Reset()
        return render(request,"Custom/reset.html",{'form':form})




def log_in(request):
   
    context= {}
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
                    login(request, user)

                    return render(request,"Custom/logout.html", {'user':user})
                else:
                    return HttpResponse("password or email is wrong")
            else:
                return  HttpResponse("NO user exists")
           
        else:
           
            return render(request, "Custom/login.html",{'form':form} )
    else:
        form = LogPage()
        context['form']  = form
        return render(request,"Custom/login.html", context)





def logout(request):

    print(request.user, "-------------------current user in session --------------------------------------")




def changepassword(request):
    if request.method == 'POST':
        form = passwordchangeform(request.POST)
       
       
        if form.is_valid():
            
            new_password = form.cleaned_data.get('new_password')
            old_password = form.cleaned_data.get('old_password')
            current_user = request.user
            
            if current_user.check_password(old_password):
                
                current_user.set_password(new_password)
                current_user.save()
            
                return HttpResponse("Password changed")
            else:
                        
                return HttpResponse("you have entered wrong password")
        else:
            form = passwordchangeform(request.POST)
            return render(request,"Custom/passwordchange.html",{'form':form})
    else:

        form = passwordchangeform()
        return render(request,"Custom/passwordchange.html",{'form':form})


def logged(request):
    logout(request)
    
    return render(request,"Custom/loggedout.html")

from  django.http import Http404
class user_api(APIView):
    def get_object(self,pk):
        try:
            usr = myUser.objects.get(pk = pk)
            return usr
        except myUser.DoesNotExist:
            raise Http404
    def get(self,request,pk,  safe = False):
       
        usr = self.get_object(pk)
        serializer = Userserializer(usr )
    


