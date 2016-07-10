from django.db import models
from django.core.urlresolvers import reverse
import tagulous
import tagulous.models
from markdownx.models import MarkdownxField
import datetime


class Source(tagulous.models.TagTreeModel):
    class TagMeta:
        space_delimiter = False

class Theme(tagulous.models.TagTreeModel):
    class TagMeta:
        initial = [
            'Арифметика',
            'Арифметика/Дроби',
            'Геометрия',
            'Геометрия/Синусы и косинусы',
            'Тригонометрия/Синусы'
        ]
        force_lowercase = True
        space_delimiter = False
        autocomplete_view = 'problem_themes_autocomplete'


class Problem(models.Model):
    # TODO: make as yield functions
    grades_ch   = [(i,i) for i in range(1,11)]  
    categories_ch = [('school', 'Школьные'), ('olymp', 'Олимпиадные'), ('science', 'Исследовательские')]
    years_ch    = [(r,r) for r in range(datetime.date.today().year, 2000, -1)]


    name        = models.CharField(u'Название', max_length=200, blank=True)
    task        = MarkdownxField()
    answer      = models.CharField(u'Ответ', max_length=200, blank=True)
    direction   = models.CharField(u'Указание', max_length=200, blank=True)
    solution    = models.TextField(u'Решение', max_length=2000, blank=True)
    grade_down  = models.IntegerField(u'От класса', choices=grades_ch)
    grade_up    = models.IntegerField(u'До класса', choices=grades_ch)
    more_info   = models.TextField(u'Дополнительная информация', max_length=2000, blank=True)

    category    = models.CharField(u'Категория', max_length=10, choices=categories_ch, default='olymp')
#    category    = tagulous.models.SingleTagField(
#                    initial="school, olymp, science",
#                    help_text="Категория"
#                  )

    theme       = tagulous.models.TagField(Theme, blank=True)

    author      = tagulous.models.TagField(space_delimiter=False, blank=True)
    book        = tagulous.models.TagField(space_delimiter=False, blank=True)

    olymp       = tagulous.models.TagField(space_delimiter=False, blank=True)
    lmsh        = tagulous.models.TagField(space_delimiter=False, blank=True)

    year        = models.IntegerField(u'Год', choices=years_ch, default=None)
    grade       = models.IntegerField(u'Класс', choices=grades_ch, default=None)
    number      = models.IntegerField(u'Номер задачи', default=None)
    

    def __str__(self):
        return self.task

class ImageSource(models.Model):
    problem = models.ForeignKey(Problem)
    source = models.FileField(upload_to='image_sources/')


#    название - rich text
#    условие - text
#    ответ - text
#    указание - text
#    решение - rich text
#    автор(ы) - tag
#    источник - tag
#    год - datetime.year
#    номер - integer
#    сложность - text
#    класс младший - integer
#    класс старший - integer
#    категория (школьные/олимпиадные/исследовательские) - tag
#    темы - hierarchy tags
#    дополнительные теги - tags
#    дополнительная информация - rich text
