from django import forms

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
    )

    end_time = forms.DateTimeField(
        label='End Time',
        required = False
    )

    description = forms.CharField(
        label='Description',
        max_length = 600,
        required=False
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('title', css_class='input-lg form-control', placeholder='Enter Event Title', style='margin-bottom: 20px'),
        Field('location', css_class='form-control', placeholder='Enter Location', style='margin-bottom: 10px'),
        Field('start_time', css_class='form-control', placeholder='Enter Start Time', style='margin-bottom: 10px'),
        Field('end_time', css_class='form-control', placeholder='Enter End Time', style='margin-bottom: 10px'),
        Field('description', css_class='form-control', placeholder='Enter Short Description of Event', style='margin-bottom: 10px'),
        FormActions(
            Submit('save_changes', 'Create', css_class="btn-primary btn-lg", style="margin-top: 10px"),
        )
   )

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
