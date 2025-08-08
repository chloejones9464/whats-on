from . import views
from django.urls import path


urlpatterns = [
    path("", views.event_list, name="event_list"),
    path("events/<int:pk>/", views.event_detail, name="event_detail"),
    path("like-event/<int:event_id>/", views.like_event, name="like_event"),
    path("my-events/", views.my_events, name="my_events"),
    path("create/", views.event_create, name="event_create"),
    path("edit/<int:pk>/", views.event_edit, name="event_edit"),
    path("delete/<int:pk>/", views.event_delete, name="event_delete"),
]
