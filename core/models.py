from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)

    def __str__(self):
        return str(self.title)

class Category(models.Model):
    post_id = models.ForeignKey("Post", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)