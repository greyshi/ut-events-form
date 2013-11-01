import datetime

from django.shortcuts import render
from django.http  import HttpResponse, HttpResponseRedirect
from django.core import serializers

from form.models import Event, Category
from form.forms import EventForm


def create(request):
    request.session['status'] = 'new'
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
            categories = form.cleaned_data['categories']
            event = Event(title=title, location=location, start_time=start_time,
                          end_time=end_time, description=description,
                          contact_name=contact_name, student_email=student_email
                         )
            event.save()
            for c in categories:
                event.categories.add(Category.objects.get(title=c))
            request.session['status'] = 'success'
            form = EventForm()  # clear the form
        else:
            request.session['status'] = 'failure'
    else:
        form = EventForm()  # an unbound form

    return render(request, 'create.html', {'form': form, 'status': request.session['status']})

def events(request):
    events = serializers.serialize("json", Event.objects.all(),
                                   fields=('title', 'location', 'description',
                                           'start_time', 'end_time', 'categories'),
                                   relations=('categories',))
    return HttpResponse(events, mimetype='application/json')

def categories(request):
    events = serializers.serialize("json", Category.objects.all())
    return HttpResponse(events, mimetype='application/json')

