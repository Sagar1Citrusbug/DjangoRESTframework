from enum import unique
from statistics import mode
from django import forms
from django.core.exceptions import ValidationError
from .models import myUser    

from django.contrib.auth.forms import UserCreationForm


class Register(UserCreationForm):
   

    class Meta:
        model = myUser
        fields = ['name','email','password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data
class LogPage(forms.Form):
    email = forms.EmailField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput())

class passwordchangeform(forms.Form):
    old_password  = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    reenter_password = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self):
        
        cleaned_data = super().clean()
        op = cleaned_data.get('old_password')
        np = cleaned_data.get('new_password')
        rep = cleaned_data.get('reenter_password')
        if op is None:
           
            self.add_error("old_password", "enter valid old password")
        if np is None:
            self.add_error("new_password", "enter valid new password")
        if rep is None:
            self.add_error("reenter_password", "type reenter password")
        if np is  not None and rep is not None and rep is not None:
            if len(np) < 8:
                self.add_error('new_password','new_password is too short')
        
            if np == op  :
                self.add_error("new_password", "new password is same as old one.")
            if rep!=np:
                self.add_error("reenter_password","mismatch")
  
        return self.cleaned_data


class forgetpass(forms.Form):
   
    email = forms.EmailField()

class Reset(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput())
    reenter_password = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self):
        
        cleaned_data = super().clean()
        
        np = cleaned_data.get('new_password')
        rep = cleaned_data.get('reenter_password')


        if np is None:
            self.add_error("new_password", "enter valid new password")
        if rep is None:
            self.add_error("reenter_password", "type reenter password")
        if np is  not None and rep is not None and rep is not None:
            if len(np) < 8:
                self.add_error('new_password','new_password is too short')
        
            
            if rep!=np:
                self.add_error("reenter_password","mismatch")
        return cleaned_data

   
