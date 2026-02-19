from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class TaskyModel(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(validators=[
      MinValueValidator(1),
      MaxValueValidator(5)  
    ])

    task = models.CharField(max_length=200)
    complished = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.priority} - {self.complished}"