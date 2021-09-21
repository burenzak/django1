from django.db import models

# Create your models here.
class Post(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    title = models.CharField(max_length=25)
    body = models.CharField(max_length=500)
    models.CharField()


    def __str__(self):
        return f"{self.title}"
