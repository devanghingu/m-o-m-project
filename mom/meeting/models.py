from django.db import models
from django.contrib.auth.models import User
# from mom.useractivity.models import 
class Meeting(models.Model):
    name        =   models.CharField(max_length=50,blank=True,default="<Untitled-Meeting>")
    meetingtext =   models.TextField(blank=True)
    user        =   models.ForeignKey(User, on_delete=models.CASCADE)
    # completed   =   models.BooleanField(default=False)
    # participate =   models.ManyToManyField("app.Model", verbose_name=_(""))

    def __str__(self):
        return self.name

class Notes(models.Model):
    description =   models.TextField(blank=True)
    meeting     =   models.ForeignKey(Meeting,on_delete=models.CASCADE)     
    shared      =   models.ManyToManyField(User, related_name='shared_notes')
    # subnotes    =   models.ForeignKey(Notes, on_delete=models.CASCADE)
