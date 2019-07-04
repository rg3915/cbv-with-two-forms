from django.db import models


class Book(models.Model):
    title = models.CharField('título', max_length=100)

    class Meta:
        ordering = ('title',)
        verbose_name = 'livro'
        verbose_name_plural = 'livros'

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField('título', max_length=100)

    class Meta:
        ordering = ('title',)
        verbose_name = 'livro'
        verbose_name_plural = 'livros'

    def __str__(self):
        return self.title
