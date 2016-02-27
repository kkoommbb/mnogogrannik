from django.db import models
from django.core.urlresolvers import reverse
import tagulous.models

grades = [(i,i) for i in range(1,11)]

class Problem(models.Model):
    name        = models.CharField(u'Название', max_length=200)
    task        = models.TextField(u'Условие', max_length=2000)
    answer      = models.CharField(u'Ответ', max_length=200, blank=True)
    direction   = models.CharField(u'Указание', max_length=200, blank=True)
    solution    = models.TextField(u'Решение', max_length=2000, blank=True)
    grade_up    = models.IntegerField(u'До класса', choices=grades)
    grade_down  = models.IntegerField(u'От класса', choices=grades)
    more_info   = models.TextField(u'Дополнительная информация', max_length=2000, blank=True)
    
    category = tagulous.models.SingleTagField(
                    initial="school, olymp, science",
                    help_text="Категория"
                  )
#    theme       = tagulous.models.TagField(
#                    tree=True,
#                    get_absolute_url=lambda tag: reverse(
#                                                    'problems.views.by_theme',
#                                                    kwargs={'theme_slug': tag.path}
#                                                )
#                    )

    def __str__(self):
        return self.task



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



# class Choice(models.Model):
#     question = models.ForeignKey(Question)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)