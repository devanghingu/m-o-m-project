from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView,View

from django.contrib.auth.forms import authenticate
from django.contrib.auth import login,logout
from django.contrib import messages

from .forms import RegistrationForm,LoginForm


class IndexTemplateView(TemplateView):
    ''' index url view render index.html '''
    template_name = 'useractivity/index.html'

class ProfileTemplateView(TemplateView):
    ''' profile url view render myprofile.html '''
    template_name = 'useractivity/myprofile.html'

class RegistrationCBView(View):
    ''' registration url view for Regisration of user '''
    def get(self,request):
        ''' bind the form in index.html file '''
        context = {'form':RegistrationForm()}
        return render(request,'useractivity/register.html',context)

    def post(self,request):
        '''
            get data from the index.html and save in db 
            Register of User
        '''
        registration_form=RegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()
            messages.success(request,'Registration Success..!!')
            return redirect('useractivity:login')
        
        return render(request,'useractivity/register.html',{'form':registration_form})


class LoginCBView(View):
    ''' login url view login thought predefine AuthenticationForm form '''
    def get(self,request):
        ''' render authentication form in index html '''
        context = {'form':LoginForm()}
        return render(request,'useractivity/login.html',context)

    def post(self,request):
        ''' authentication of user and render the home html '''
        login_form=LoginForm(request=request,data=request.POST)
    
        if login_form.is_valid():
            user = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user=authenticate(username=user,password=password)

            if user:
                login(request,user)
                return redirect('useractivity:index')
            else:
                context = {'form':login_form}
                messages.error(request,'Oops..!! Invalid username and password ')
                return render(request,'useractivity/login.html',context)
        messages.error(request,"Invalid Input Please Enter Valid information")
        return render(request,'useractivity/login.html',{'form':login_form})

class LogoutCBView(View):
    ''' logout url view,'''
    def get(self,request):
        ''' Logout the user '''
        messages.success(request,'Logout Success.!!')
        logout(request)
        return redirect('useractivity:login')