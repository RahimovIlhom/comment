from django.db import models


# Create your models here.

class Comment(models.Model):
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=20, null=True, blank=True)
    field = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.comment
