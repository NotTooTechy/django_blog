from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
'''
_posts = [
    {'author': "Albert S.", "title": "Blog Post 1", "content": "First post content", "date_posted":"February 1, 2020"},
    {'author': "Joe D.", "title": "Blog Post 2", "content": "Second post content", "date_posted":"March 1, 2020"},
    {'author': "Will S.", "title": "Blog Post 3", "content": "Third post content", "date_posted":"March 2, 2020"}
]
'''
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # One to many, one user many posts
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
