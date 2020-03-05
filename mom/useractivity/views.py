from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.generic import TemplateView,View

from django.contrib.auth.forms import authenticate
from django.contrib.auth import login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import RegistrationForm,LoginForm,ProfileForm,Change_passwordForm
from .models import Profile

class IndexTemplateView(TemplateView):
    ''' index url view render index.html '''
    template_name = 'useractivity/index.html'

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


@method_decorator(login_required,name='dispatch')
class ChangePasswordCBView(View):
    ''' change_password url view '''
    def post(self,request):
        ''' change password when post req'''
        pass_chng_form = Change_passwordForm(request.user,request.POST)
        if pass_chng_form.is_valid():
            user=pass_chng_form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Password Was Successfully Updated..!!')
            return redirect('useractivity:profile')
        else:
            messages.error(request,'Please Correct the error below.')
            context={'form':ProfileForm(instance=request.user.profile)}
            context['passwordform'] = pass_chng_form
            context['passwordtab']='passwordtab'
        return render(request,'useractivity/myprofile.html',context)


@method_decorator(login_required,name='dispatch')        
class ProfileCBView(View):
    ''' profile url view render myprofile.html '''
    def get(self,request):
        context={'form':ProfileForm(instance=request.user.profile)}
        context['passwordform'] = Change_passwordForm(request.user)
        return render(request,'useractivity/myprofile.html',context)

    def post(self,request):        
        profile_form = ProfileForm(request.POST or None,instance=request.user.profile)
        if profile_form.is_valid():
            user=profile_form.save(commit=False)
            user.user=request.user
            user.save()
            messages.success(request,"Profile Information Updated..!!")
            return redirect('useractivity:profile')

        return render(request,'useractivity/myprofile.html',{'form':profile_form})

@method_decorator(login_required,name='dispatch')
class Profile_uploadCBView(View):
   
    def post(self,request):

        if request.user.is_authenticated:
            request.user.profile.profile=request.FILES['image']
            request.user.profile.save()
            return JsonResponse(status=200,data={'url':request.user.profile.profile.url})
        else:
            return JsonResponse(status=203,data={'error':'unauthorize request.!!'})
            