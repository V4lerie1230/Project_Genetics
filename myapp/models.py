from django.db import models

# Create your models here.


class Mutation(models.Model):
    name = models.CharField(max_length=30)
    secuence = models.CharField(max_length=30) 

    def __str__(self):
        return self.name



class Diseases(models.Model):
    name = models.CharField(max_length=30)
    probability = models.CharField(max_length=30) 
    description = models.CharField(max_length=30) 

    def __str__(self):
        return self.name
