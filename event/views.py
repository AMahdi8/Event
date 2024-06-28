from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from datetime import datetime, timedelta


from .models import Event


def upcoming_events(request):
    upcoming_event = Event.objects.filter(
        date__gte=datetime.now()).order_by('-date')
    past_7_days_event = Event.objects.filter(date__lt=datetime.now()).filter(
        date__gte=datetime.now()-timedelta(days=7))

    url = request.build_absolute_uri()
    context = {
        "future_events": upcoming_event,
        "past_events": past_7_days_event,
        "url": url
    }

    return render(request, 'event/upcoming_events.html', context=context)


def event(request, pk):
    event = get_object_or_404(Event, id=pk)
    context = {
        "event": event
    }
    return render(request, 'event/event.html', context=context)
