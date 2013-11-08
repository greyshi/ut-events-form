import datetime

from django.shortcuts import render, get_object_or_404
from django.http  import HttpResponse, HttpResponseRedirect
from django.core import serializers

from form.models import Event, Category
from form.forms import EventForm


def home(request):
    return render(request, 'home.html')



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
    event_list = Event.objects.filter(start_time__gte=datetime.datetime.now()).order_by('start_time')
    if request.META.get('HTTP_ACCEPT') == 'application/json':
        serialized_events = serializers.serialize("json", event_list,
                                                  fields=('title', 'location', 'description',
                                                  'start_time', 'end_time', 'categories'),
                                                  relations=('categories',))
        return HttpResponse(serialized_events, mimetype='application/json')
    return render(request, 'events.html', {'events': event_list})

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'detail.html', {
        'event': event,
    })

def categories(request):
    events = serializers.serialize("json", Category.objects.all())
    return HttpResponse(events, mimetype='application/json')

