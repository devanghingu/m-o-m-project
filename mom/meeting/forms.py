from django import forms
from django.contrib.auth.models import User
from .models import Meeting,Notes

class meetingname(forms.ModelForm):
    class Meta:
        model =Meeting
        fields =['name','meetingtext']
        # widget = {'meetingtext':forms.HiddenInput()}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control mb-2','placeholder':'Give Small title to your meeting'})
        self.fields['meetingtext'].widget=forms.HiddenInput()
        
    
    def clean_name(self):
        ''' check if name has minium length '''
        name = self.cleaned_data["name"]
        if(len(str(name))<=5):
            raise forms.ValidationError('Name should aleast 6 character')
        return name
            
    