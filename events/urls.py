from . import views
from django.urls import path

urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('my-events/', views.my_events, name='my_events'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
]