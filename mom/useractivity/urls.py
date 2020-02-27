from django.urls import path
from django.conf.urls import url

from .views import IndexTemplateView,RegistrationCBView,LoginCBView,LogoutCBView,ProfileTemplateView

app_name="useractivity"

urlpatterns = [

    path('',IndexTemplateView.as_view(),name='index'),
    path('registration',RegistrationCBView.as_view(),name='registration'),
    path('login',LoginCBView.as_view(),name='login'),
    path('logout',LogoutCBView.as_view(),name='logout'),
    path('profile',ProfileTemplateView.as_view(),name='profile'),
]
