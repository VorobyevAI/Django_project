from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=30)
    intro = models.CharField('Превью', max_length=100)
    text = models.TextField('Текс новости')
    data = models.DateTimeField('Время публикпции')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'