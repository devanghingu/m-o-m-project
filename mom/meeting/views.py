from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from . import forms
from .models import Meeting,Notes
import json
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required

@method_decorator(login_required,name='dispatch')
class MeetingStartCBView(View):
    ''' Starting Page '''
    def get(self,request,*args, **kwargs):
        if(Meeting.meeting_not_completed(self,meeting_id=kwargs['meeting_id'])):
            return render(request,'useractivity/index.html')

@method_decorator(login_required,name='dispatch')
class MeetingtextCBView(View):
    ''' Meeting Text Displaying '''  
    def get(self,request,*args, **kwargs):
        context={}
        data=Meeting.objects.filter(id=kwargs['meeting_id'],user=request.user)
        if(data):
            context['meetingdata'] = data[0]
            context['notes']       = serialize('json',Notes.objects.filter(meeting=data[0])) 
            return render(request,'meeting/meetingtext.html',context)
        else:
            messages.info(request,"opps..!! meeting doesn't exist ")
            return redirect('useractivity:index')
    
    def post(self,request,*args, **kwargs):
        print('MeetingtextCBView : POST')
        meeting             =  Meeting.objects.get(pk=kwargs['meeting_id'])
        meeting.name        =  request.POST['meetingname']
        meeting.meetingtext =  request.POST['meetingtext']
        meeting.save()
        notes               = [x.id for x in Notes.objects.filter(meeting=meeting)]
        print(notes)
        # convert str to int of id and get not from request.POST['note'] and evalute them 
        new_notes           = dict(map(lambda x:(int(x[0]),x[1]),eval(request.POST['meetingtnote']).items())) 
        for i in new_notes: 
            if i in notes:
                note = Notes.objects.get(pk=i)
                note.description = new_notes[i] 
                note.save()
                notes.remove(i)
            else:
                note = Notes.objects.create(description=new_notes[i],meeting=meeting)

        if len(notes)>0:
            for i in notes:
                note = Notes.objects.get(pk=i).delete()
                print(note)
                
        return redirect('meeting:meetingtext',meeting_id=kwargs['meeting_id'])

@method_decorator(login_required,name='dispatch')   
class ShowallMettingCBView(View):
    ''' To show all meeting '''
    #login required decorators
    def get(self,request):
        context={}
        context['allmeeting']=Meeting.objects.filter(user=request.user)
        return render(request,'meeting/meeting_all.html',context)

    #login required decorators
    def post(self,request):
        pass
    
@method_decorator([login_required,csrf_exempt], name='dispatch')
class SaveMeetingCBView(View):
    #login required decorators
    def get(self,request):
        return render(request,'meeting/meeting_save.html',{'meetingname':forms.meetingname()})
        
    def post(self,request):
        print('SaveMeetingCBView : POST')
        if request.is_ajax():
            meeting_id = Meeting.objects.create(meetingtext=request.POST['meeting_text'],user=request.user)
            return JsonResponse(status=200,data={"meeting_id":meeting_id.id})
        else:
            return JsonResponse(status=203,data={"error": "unauthorize request.!!"})

@method_decorator(login_required,name='dispatch')
class DeleteMeetingCBView(View):
    ''' Meeting Delete View '''  
    def get(self,request,*args, **kwargs):
        Meeting.objects.filter(user=request.user,pk=kwargs['meeting_id']).delete()
        return redirect('meeting:allmeeting')