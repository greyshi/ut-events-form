from django.shortcuts import render

from form.models import Event, Category
from form.forms import EventForm

def create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = Event(title=form.cleaned_data['title'])
            event.save()
            """
            for c in ['choice{0}'.format(i) for i in range(1, 5)]:
                try:
                    text = form.cleaned_data[c]
                except KeyError:
                    break
                if text:
                    event.choice_set.create(choice_text=text)
            """
            return HttpResponseRedirect('/')
    else:
        form = EventForm()  # an unbound form

    return render(request, 'create.html', {'form': form})
