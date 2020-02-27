from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    
    class Meta:
        model   = User
        fields  = ['first_name','last_name','username','email','password1','password2']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control','placeholder':self.fields[field].label})
        
        
class LoginForm(AuthenticationForm):

    class Meta:
        model=User
        fields=['username','password']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control','placeholder':self.fields[field].label})