from django import forms
from .models import Event
from django_summernote.widgets import SummernoteWidget
from .models import Comment


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'image',
            'title',            
            'excerpt',
            'description',
            'date',
            'location',
        ]
        widgets = {
            'description': SummernoteWidget(),
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Leave a comment...'}),
        }
        
