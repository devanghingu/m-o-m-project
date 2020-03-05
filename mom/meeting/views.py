from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from django.contrib import messages
from . import forms
from .models import Meeting, Notes
class MeetingtextCBView(View):
        
    def get(self,request,*args, **kwargs):
        context={}
        data=Meeting.objects.filter(id=kwargs['meeting_id'],user=request.user)
        if(data):
            context['meetingdata']=data[0]
            return render(request,'meeting/meetingtext.html',context)
        else:
            messages.info(request,"opps..!! meeting doesn't exist ")
            return redirect('useractivity:index')

    def post(self,request):
        pass


class ShowallMettingCBView(View):
    ''' To show all meeting '''
    #login required decorators
    def get(self,request):
        pass
        # return render(request,'meeting/meetingtext.html')
    #login required decorators
    def post(self,request):
        pass


class SaveMeetingCBView(View):
    #login required decorators
    def get(self,request):
        return render(request,'meeting/meeting_save.html',{'meetingname':forms.meetingname()})
    #login required decorators
    def post(self,request):
        meetingname=forms.meetingname(request.POST)
        if request.user.is_authenticated and meetingname.is_valid():
            meeting=meetingname.save(commit=False)
            meeting.user=request.user
            meeting.save()
            return redirect('meeting:meetingtext',meeting_id=meeting.id)
        return render(request,'meeting/meeting_save.html',{'meetingname':meetingname})

                        