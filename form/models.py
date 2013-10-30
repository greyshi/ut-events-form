import datetime

from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"


class Event(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    start_time = models.DateTimeField('start of event', auto_now_add=True)
    end_time = models.DateTimeField('end of event', auto_now_add=True)
    categories = models.ManyToManyField(Category)
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()

    def __unicode__(self):
        return self.title

    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=7)

    published_recently.boolean = True
    published_recently.admin_order_field = 'pub_date'

    class Meta:
        ordering = ['pub_date']
        verbose_name_plural = "Entries"

