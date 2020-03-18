from django.urls import path
from django.conf.urls import url
from . import views

app_name="meeting"

urlpatterns = [
    path('start/meeting_id=<int:meeting_id>',views.MeetingStartCBView.as_view(),name='start'),
    path('<int:meeting_id>/text',views.MeetingtextCBView.as_view(),name='meetingtext'), #update meeting and create it's note
    path('<int:meeting_id>/notes',views.ShowAllNotesCBView.as_view(),name='meetingnotes'),
    path('<int:meeting_id>/notes/share',views.ShowAllNotesCBView.as_view(),name='meetingnotes'),
    path('all',views.ShowallMettingCBView.as_view(),name='allmeeting'), # to show all meeting 

    path('save',views.SaveMeetingCBView.as_view(),name='savemeeting'),  # to save recent create meeting
    path('<int:meeting_id>/delete',views.DeleteMeetingCBView.as_view(),name='deletemeeting'),
    path('sharenote',views.ShareNoteCBView.as_view(),name='sharenote'),  # to call ajax for shared note with user
    path('searchuser',views.SearchUserCBView.as_view(),name='searchuser'),
]