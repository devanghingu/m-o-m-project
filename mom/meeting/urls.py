from django.urls import path
from django.conf.urls import url
from . import views

app_name="meeting"

urlpatterns = [
    path('<int:meeting_id>/text',views.MeetingtextCBView.as_view(),name='meetingtext'),
    path('all',views.ShowallMettingCBView.as_view(),name='allmeeting'), # to show all meeting 
    path('save',views.SaveMeetingCBView.as_view(),name='savemeeting'),  # to save recent create meeting 
]