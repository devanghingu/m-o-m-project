from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic import View


@method_decorator(login_required, name="dispatch")
class MeetingtextCBView(View):
    def get(self, request):
        return render(request, "meeting/meetingtext.html")

    def post(self, request):
        pass
