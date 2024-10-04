from django.db import models

# Create your models here.


class Skills(models.Model):
    label = models.CharField(max_length = 150)
    level= models.IntegerField()
    
    def __str__(self):
        return self.label