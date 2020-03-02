from django.urls import path
from django.conf.urls import url
from .views import MeetingtextCBView

app_name="meeting"

urlpatterns = [
    path('meetingtext',MeetingtextCBView.as_view(),name='meetingtext'),
]