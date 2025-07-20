from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.db.models import Q
from .models import Event, Comment
from .forms import EventForm, CommentForm
from django.utils import timezone

# Create your views here.
class EventList(generic.ListView):
    queryset = Event.objects.all()
    template_name = 'events/index.html'
    paginate_by = 6  # Number of events per page   
    
    def get_queryset(self):
        queryset = Event.objects.filter(date__gte=timezone.now()).order_by('date')
        location = self.request.GET.get('location')
        date = self.request.GET.get('date')
        organizer = self.request.GET.get('organizer')
        if location:
            queryset = queryset.filter(location__iexact=location)
        if date:
            queryset = queryset.filter(date=date)
        if organizer:
            queryset = queryset.filter(organizer__username__iexact=organizer)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add list of locations for the dropdown
        context['locations'] = Event.objects.values_list('location', flat=True).distinct()
        return context
    
@login_required
def my_events(request):
    liked_events = request.user.liked_events.all()
    created_events = Event.objects.filter(organizer=request.user)

    return render(request, 'events/my_events.html', {
        'liked_events': liked_events,
        'created_events': created_events,
    })
    

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Event  

@login_required
def event_list(request):
    events = Event.objects.all()
    
    # Get filter values from GET request
    selected_date = request.GET.get('date')
    selected_location = request.GET.get('location')
    selected_organizer = request.GET.get('organizer')

    # Apply filters if present
    if selected_date:
        events = events.filter(date=selected_date)
    if selected_location:
        events = events.filter(location__icontains=selected_location)
    if selected_organizer:
        events = events.filter(
            organizer__username__icontains=selected_organizer
        )

    return render(request, 'events/event_list.html', {
        'events': events,
        'selected_date': selected_date,
        'selected_location': selected_location,
        'selected_organizer': selected_organizer,
    })



@login_required
def like_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.user in event.liked_by.all():
        event.liked_by.remove(request.user)  # un-like
    else:
        event.liked_by.add(request.user)  # like

    return redirect(request.META.get('HTTP_REFERER', 'home'))  # go back to previous page
   
    
@login_required
def event_create(request):
    # Only allow pubs to access this
    if not hasattr(request.user, 'profile') or request.user.profile.user_type != 'organiser':
        return redirect('event_list')

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('my_events') 
    else:
        form = EventForm()

    return render(request, 'events/event_form.html', {'form': form})


@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk, organizer=request.user)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('my_events')
    else:
        form = EventForm(instance=event)

    return render(request, 'events/event_form.html', {'form': form})

@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk, organizer=request.user)
    
    if request.method == 'POST':
        event.delete()
        return redirect('my_events')
    
    return redirect('my_events')

@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    comments = event.comments.filter(approved=True)
    form = CommentForm()
    editing_comment_id = None
    
    if request.user.is_authenticated:
        comments = event.comments.filter(Q(approved=True) | Q(user=request.user)).order_by('-posted_at')
    else:
        comments = event.comments.filter(approved=True).order_by('-posted_at')

    
    if request.method == 'POST':
        if 'delete_comment' in request.POST:
            comment_id = request.POST['delete_comment']
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
            comment.manually_edited = True
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
    