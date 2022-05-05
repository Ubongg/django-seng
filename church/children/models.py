from django.db import models

# Create your models here.

class Children(models.Model):
 name = models.CharField(max_length = 100)
 thumb = models.ImageField(blank=True)

 def __str__(self):
  return self.name
