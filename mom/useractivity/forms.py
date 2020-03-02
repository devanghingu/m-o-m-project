from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from useractivity.models import Profile

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