from django.contrib import admin

from models import Event, Category

class EventAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    search_fields = ['title', 'description', 'contact_name', 'student_email']
    date_hierarchy = 'pub_date'

admin.site.register(Event, EventAdmin)
admin.site.register(Category)
