from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    notes = models.TextField()
    status = models.BooleanField()
    end_time = models.DateTimeField(blank=True, null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
