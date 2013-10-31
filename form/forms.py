from django import forms
from django.contrib.admin import widgets
from django.utils.formats import get_format

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class EventForm(forms.Form):
    title = forms.CharField(
        label='Title',
        max_length=255
    )

    location = forms.CharField(
        label='Location',
        max_length=255
    )

    start_time = forms.DateTimeField(
        label='Start Time',
        input_formats=['%m/%d/%Y %I:%M%p',],
    )

    end_time = forms.DateTimeField(
        label='End Time',
        input_formats=['%m/%d/%Y %I:%M%p',],
        required = False
    )

    description = forms.CharField(
        label='Description',
        max_length=600,
        widget=forms.Textarea,
        required=False
    )

    contact_name = forms.CharField(
        label='Contact Name',
        max_length=255
    )

    student_email = forms.EmailField(
        label='Student Email',
        max_length=255
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('title', css_class='input-lg form-control', placeholder='Enter Event Title'),
        Field('location', css_class='form-control', placeholder='Enter Location'),
        Field('start_time', css_class='form-control', placeholder='Enter Start Time'),
        Field('end_time', css_class='form-control', placeholder='Enter End Time'),
        Field('description', css_class='form-control', placeholder='Enter an Event Description'),
        Field('contact_name', css_class='form-control', placeholder='Enter your name (will be kept private)'),
        Field('student_email', css_class='form-control', placeholder='Enter a valid utexas.edu email address (will be kept private)'),
        FormActions(
            Submit('save_changes', 'Create', css_class="btn-primary btn-lg", style="margin-top: 25px"),
        )
   )

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
