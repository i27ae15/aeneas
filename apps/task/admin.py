from django.contrib import admin

from .models import Task, Section, Objective

admin.site.register([Task, Section, Objective])
