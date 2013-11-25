from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from form.models import Event, Category


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        authorization= Authorization()
        allowed_methods = ['get', 'post']


class EventResource(ModelResource):
    categories = fields.ToManyField(CategoryResource, 'categories')

    class Meta:
        queryset = Event.objects.all()
        resource_name = 'events'
        authorization= Authorization()
        allowed_methods = ['get', 'post']
        ordering = ['pub_date', 'start_time', 'end_time', 'title']
        filtering = {
            'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
            'start_time': ['exact', 'lt', 'lte', 'gte', 'gt'],
            'end_time': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
        excludes = ['student_email', 'is_verified', 'confirmation_code']
