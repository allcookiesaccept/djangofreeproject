from django.db import models


class Article(models.Model):
    title = models.CharField('Название', max_length=250, default='Новость дня')
    description = models.CharField('Название', max_length=250, default='Новость дня')
    text = ''
    date = ''