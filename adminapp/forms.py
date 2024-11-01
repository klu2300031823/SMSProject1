from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title']

from django import forms
from .models import StudentList

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']

from django import forms
class UploadFileForm(forms.Form):
    file = forms.FileField()

# forms.py
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'phone', 'email', 'feedback']
        widgets = {
            'feedback': forms.Textarea(attrs={'maxlength': 160}),
        }

from .models import ConMan

class ConManForm(forms.ModelForm):
    class Meta:
        model=ConMan
        fields=['name','phone','email','address']