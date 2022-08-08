from datetime import timezone
from django.db import models
from django.conf import settings
from django.utils import timezone
from empresas.models import Post

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    local_arm = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    text = models.TextField()
    dat = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title