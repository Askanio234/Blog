from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Enter your bio here")

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    name = models.CharField(max_length=200, help_text="Blog's name")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=500, help_text="Post text")
    date = models.DateField(default=date.today)

    class Meta:
        ordering = ["-post_date"]

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=1000, help_text="Enter  your comment")
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        len_title = 75
        if len(self.text) > len_title:
            titlestring = self.text[:len_title] + '...'
        else:
            titlestring = self.text
        return titlestring
