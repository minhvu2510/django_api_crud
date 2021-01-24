from django.db import models


class Word(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    word = models.CharField(max_length=100, blank=True)
    mean = models.TextField()
    topic = models.CharField(max_length=100, blank=True, default='other')
    level = models.IntegerField(max_length=10, blank=True, default=10)
    favorite = models.BooleanField(default=False)
    class Meta:
        ordering = ['level']

class Topic(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=100, blank=True)
    level = models.IntegerField(max_length=10, blank=True, default=10)
    favorite = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']
