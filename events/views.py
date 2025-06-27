from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Event
from .forms import EventForm

# Create your views here.
class EventList(generic.ListView):
    queryset = Event.objects.all()
    template_name = 'events/index.html'
    paginate_by = 6  # Number of events per page   
    
    
@login_required
def my_events(request):
    # Only allow pubs to access this
    if not hasattr(request.user, 'profile') or request.user.profile.user_type != 'pub':
        return redirect('event_list')

    events = Event.objects.filter(organizer=request.user).order_by('-date')
    return render(request, 'events/my_events.html', {'events': events})
    


@login_required
def event_list(request):
    # Everyone can see this
    return render(request, 'events/event_list.html')
    
@login_required
def create_event(request):
    # Only allow pubs to access this
    if not hasattr(request.user, 'profile') or request.user.profile.user_type != 'pub':
        return redirect('event_list')  # or show a "permission denied" page

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('my_events')  # or event detail page
    else:
        form = EventForm()

    return render(request, 'events/create_event.html', {'form': form})