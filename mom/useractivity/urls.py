from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from mom import settings
from .views import IndexTemplateView,RegistrationCBView,LoginCBView,LogoutCBView,ProfileCBView,Profile_uploadCBView,ChangePasswordCBView

app_name="useractivity"

urlpatterns = [
    path('',IndexTemplateView.as_view(),name='index'),
    path('registration',RegistrationCBView.as_view(),name='registration'),
    path('login',LoginCBView.as_view(),name='login'),
    path('logout',LogoutCBView.as_view(),name='logout'),
    path('profile',ProfileCBView.as_view(),name='profile'),
    path('profile_upload',Profile_uploadCBView.as_view(),name='profile_upload'),
    path('change_password',ChangePasswordCBView.as_view(),name='change_password'),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)