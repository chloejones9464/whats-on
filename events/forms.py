from django import forms
from .models import Event
from django_summernote.widgets import SummernoteWidget

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location']
        widgets = {
            'description': SummernoteWidget(),
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
