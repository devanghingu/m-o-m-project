from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.generic import TemplateView,View

class MeetingtextCBView(View):

    def get(self,request):
        return render(request,'meeting/meetingtext.html')

    def post(self,request):
        pass
