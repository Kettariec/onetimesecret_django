from django.contrib import admin
from onetimesecret.models import Secret


@admin.register(Secret)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'text', 'time', 'days',)
