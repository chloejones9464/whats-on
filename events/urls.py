from . import views
from django.urls import path

urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('my-events/', views.my_events, name='my_events'),
    path('create/', views.create_event, name='create_event'),
    path('events/', views.event_list, name='event_list'),
]