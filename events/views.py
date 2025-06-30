from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Event
from .forms import EventForm, CommentForm

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


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    comments = event.comments.filter(approved=True)
    form = CommentForm()
    editing_comment_id = None
    
    if request.method == 'POST':
        if 'delete_comment_id' in request.POST:
            comment_id = request.POST['delete_comment_id']
            comment = get_object_or_404(Comment, id=comment_id, user=request.user)
            comment.delete()
            return redirect('event_detail', pk=pk)
        
        elif 'edit_comment_id' in request.POST:
            editing_comment_id = int(request.POST['edit_comment_id'])
        
        elif 'updated_content' in request.POST:
            comment_id = request.POST.get('comment_id')
            updated_text = request.POST.get('updated_content')
            comment = get_object_or_404(Comment, id=comment_id, user=request.user)
            comment.content = updated_text
            comment.save()
            return redirect('event_detail', pk=pk)
        
        else:       
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.event = event
                comment.user = request.user
                comment.save()
                return redirect('event_detail', pk=event.pk)
             
    return render(request, 'events/event_detail.html', {
       'event': event,
       'comments': comments,
       'form': form,
       'editing_comment_id': editing_comment_id,
    })