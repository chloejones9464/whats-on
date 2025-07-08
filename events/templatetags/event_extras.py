from django import template
from datetime import datetime

register = template.Library()

@register.filter
def future_events(events):
    """Return only events with a date in the future."""
    return events.filter(date__gte=datetime.now())
