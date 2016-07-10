from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from markdownx.widgets import AdminMarkdownxWidget

import tagulous.admin

from . import models

class HorizRadioRenderer(forms.RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class ImageSourceInline(admin.StackedInline):
    model = models.ImageSource
    extra = 1


class ProblemAdminForm(forms.ModelForm):
    class Meta:
        model = models.Problem
        fields = '__all__'
        widgets = {
            'task': AdminMarkdownxWidget,
            'category': forms.RadioSelect,
            'grade_up': forms.RadioSelect(renderer=HorizRadioRenderer),
            'grade_down': forms.RadioSelect(renderer=HorizRadioRenderer),
        }

class ProblemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    form = ProblemAdminForm
    inlines = [ImageSourceInline]

    class Media:
        css = {'all': ('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.5.1/katex.min.css',)}
        js = (
                'https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.1/jquery.min.js',
                'https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.5.1/katex.min.js', 
            )


tagulous.admin.register(models.Problem, ProblemAdmin)

tagulous.admin.register(models.Theme)