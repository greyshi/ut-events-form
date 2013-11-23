from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from form.models import Event, Category


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        authorization= Authorization()
        allowed_methods = ['get']


class EventResource(ModelResource):
    categories = fields.ToManyField(CategoryResource, 'categories')

    class Meta:
        queryset = Event.objects.all()
        resource_name = 'events'
        authorization= Authorization()
        allowed_methods = ['get', 'post']
