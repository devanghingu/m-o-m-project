from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from mom import settings
from .views import IndexTemplateView, RegistrationCBView, LoginCBView, LogoutCBView, ProfileCBView, Profile_uploadCBView, ChangePasswordCBView
from django.contrib.auth import views as auth_views

app_name = "useractivity"

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('registration', RegistrationCBView.as_view(), name='registration'),
    path('login', LoginCBView.as_view(), name='login'),
    path('logout', LogoutCBView.as_view(), name='logout'),
    path('profile', ProfileCBView.as_view(), name='profile'),
    path('profile_upload', Profile_uploadCBView.as_view(), name='profile_upload'),
    path('change_password', ChangePasswordCBView.as_view(), name='change_password'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset.html',
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             success_url='/password-reset/done/',
         ),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html',

         ),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html',
             success_url='/password-reset-complete'
         ),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
