from django.db import models
from django.shortcuts import reverse


class New(models.Model):
    CATEGORIES_CHOICES = [('uncos', 'Новости'), ('articles', 'Статьи')]

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORIES_CHOICES, default='uncos')
    data_pub = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{}'.format(self.title)
