from django.db import models
from django.contrib.auth.models import User
# from mom.useractivity.models import 
class Meeting(models.Model):
    name        =   models.CharField(max_length=50,blank=True)
    meetingtext =   models.TextField(blank=True)
    user        =   models.ForeignKey(User, on_delete=models.CASCADE)
    completed    =   models.BooleanField(default=False)
    # participate =   models.ManyToManyField("app.Model", verbose_name=_(""))
    def __str__(self):
        return self.name

    def meeting_not_completed(self,meeting_id = None):
        if meeting_id!=None:
            data=Meeting.objects.filter(id=meeting_id, completed=False)
            if(data):
                return data
            else:
                return False
        else:
            return False
            
class Notes(models.Model):
    name        =   models.CharField(max_length=50,blank=True)
    description =   models.TextField(blank=True)
    meeting     =   models.ManyToManyField(Meeting)
    # subnotes    =   models.ForeignKey(Notes, on_delete=models.CASCADE)
