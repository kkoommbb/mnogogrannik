from django.db import models

class Problem(models.Model):
    name        = models.CharField(u'Название', max_length=200)
    task        = models.TextField(u'Условие', max_length=2000)
    answer      = models.CharField(u'Ответ', max_length=200)
    direction   = models.CharField(u'Указание', max_length=200)
    solution    = models.TextField(u'Решение', max_length=2000)

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