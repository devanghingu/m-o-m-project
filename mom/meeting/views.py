from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name="dispatch")
class MeetingtextCBView(View):
    def get(self, request):
        return render(request, "meeting/meetingtext.html")

    def post(self, request):
        pass
