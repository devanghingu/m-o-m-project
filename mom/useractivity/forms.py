from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms

class RegistrationForm(UserCreationForm):
    
    class Meta:
        model   = User
        fields  = ['first_name','last_name','username','email','password1','password2']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control','placeholder':self.fields[field].label})
        
    def clean_first_name(self):
        firstname=self.cleaned_data['first_name']
        if len(firstname) <=0:
            raise forms.ValidationError("First Name should not blank")
        return firstname
    def clean_last_name(self):
        lastname=self.cleaned_data['last_name']
        if len(lastname) <=0:
            raise forms.ValidationError("last_name should not blank")        
        return lastname

class LoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control','placeholder':self.fields[field].label})

class ProfileForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=('bio','company','designation')

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control','placeholder':self.fields[field].label})
        self.fields['bio'].widget.attrs.update({'rows':3})
        
class Change_passwordForm(PasswordChangeForm):

    class Meta:
        model = User
        fields= ('old_password','new_password1','new_password2')

    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        for field in self.fields:
          self.fields[field].widget.attrs.update({'class':'form-control','placeholder':self.fields[field].label})