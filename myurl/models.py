from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class MyURL(models.Model):
    owner = models.ForeignKey(User, on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('myurl-detail',kwargs={'pk': self.pk})
