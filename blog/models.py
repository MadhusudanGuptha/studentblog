
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    student_name = models.CharField(max_length=100)
    your_opinion = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})