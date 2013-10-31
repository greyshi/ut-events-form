import datetime

from django.shortcuts import render
from django.http  import HttpResponse, HttpResponseRedirect
from django.core import serializers

from form.models import Event, Category
from form.forms import EventForm


def create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            location = form.cleaned_data['location']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data.get('end_time')
            description = form.cleaned_data.get('description')
            contact_name = form.cleaned_data['contact_name']
            student_email = form.cleaned_data['student_email']
            event = Event(title=title, location=location, start_time=start_time,
                          end_time=end_time, description=description,
                          contact_name=contact_name, student_email=student_email
                         )
            event.save()
            return HttpResponseRedirect('/')
    else:
        form = EventForm()  # an unbound form

    return render(request, 'create.html', {'form': form})

def events(request):
    events = serializers.serialize("json", Event.objects.all(),
                                   fields=('title', 'location', 'description',
                                           'start_time', 'end_time', 'categories'))
    return HttpResponse(events, mimetype='application/json')

