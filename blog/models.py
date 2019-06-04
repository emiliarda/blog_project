from django.db import models
from django.utils import timezone

class Category(models.Model):
    class Meta:
            verbose_name_plural = 'Categories'

        name = models.CharField(max_length=100)
        description = models.CharField(max_length=300)
        imagefile = models.CharField(max_length=300)
        def __str__(self):
            return self.name

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    def approve(self):
        self.approved_comment = True
        self.save()
    def __str__(self):
        return self.text