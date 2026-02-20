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

    task = models.TextField(max_length=200)
    complished = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return f"{self.title} - {self.priority} - {self.complished}"
    
    class Meta:
        verbose_name = 'Tasky Model'
        verbose_name_plural = 'Tasky Model'



class ComplishedTaskModel(models.Model):
    title = models.CharField(max_length=50)
    date = models.CharField(max_length=70)
    priority = models.IntegerField()
    task = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}| ⭐{self.priority}"
    
    