from django.contrib import admin

import tagulous.admin

from .models import Problem

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
tagulous.admin.register(Problem, PersonAdmin)