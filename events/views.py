from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Event

# Create your views here.
class EventList(generic.ListView):
    queryset = Event.objects.all()
    template_name = 'events/index.html'
    paginate_by = 2  # Number of events per page    
    
