from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from . import forms
from .models import Meeting,Notes
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail 
# import json
from django.core.serializers import serialize

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

@method_decorator(login_required,name='dispatch')
class ShowAllNotesCBView(View):
    def get(self,request,*args, **kwargs):
        context={}
        context['alluser']=User.objects.filter(is_superuser=False).exclude(username=request.user)
        context['allnotes']=Notes.objects.filter(meeting=kwargs['meeting_id'],meeting__user=request.user)
        return render(request,'meeting/meeting_notes_all.html',context)
    def post(self,request,*args, **kwargs):
        context={}
        note_id=request.POST.get('note_id')
        note=Notes.objects.filter(id=note_id,meeting=kwargs['meeting_id'],meeting__user=request.user).get()
        alluser=request.POST.getlist('users')

        if note:
            for user in map(int,alluser[0].split(',')):
                user=User.objects.get(id=user)
                if(user):
                    note.shared.add(user)
                    message = Mail( from_email='info@mom.com',
                                    to_emails=user.email,
                                    subject='{0} is shared notes with you'.format(request.user),
                                    html_content="""<strong>
                                        Hello {0},
                                            <u>{1}</u> is shared notes with you,<br/> 
                                            You can check all notes at your accounts.<br/>
                                        Thanks. 
                                    </strong>""".format(user.get_full_name(),request.user.first_name))
                    try:
                        sg = SendGridAPIClient('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')
                        response = sg.send(message)
                        print(response.status_code," done")
                        
                    except Exception as e:
                        print(e.message)
                        return JsonResponse(context,safe=False)
                        
        context['message1']='done'
        note.save()
        return JsonResponse(context,safe=False)


@method_decorator(login_required,name='dispatch')
class ShareNoteCBView(View):
    def get(self,request,*args, **kwargs):
        query = request.GET.get('q', None)
        if query:
            alluser = User.objects.filter(Q(first_name__startswith=query)|Q(username__startswith=query)|Q(email__startswith=query),is_superuser=False).exclude(username=request.user)
            results  = list(map(lambda x:{'id':x.pk,'text':x.get_full_name()} ,alluser))
            return JsonResponse(results,safe=False)
        else:
            return JsonResponse(data={'success': False,'errors': 'No mathing items found'})

@method_decorator(login_required,name='dispatch')
class SearchUserCBView(View):
    def get(self,request,*args, **kwargs):
        note_id = request.GET.get('notes_id',None)
        if note_id:
            alluser = Notes.objects.get(id=note_id).shared.all()
            results  = list(map(lambda x:{'id':x.pk,'text':x.get_full_name()} ,alluser))
            return JsonResponse(results,safe=False)
        else:    
            return JsonResponse(data={'errors': 'Notes not share..!'})


    