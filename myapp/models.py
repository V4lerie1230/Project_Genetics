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

class Crossing(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30) 
    result = models.CharField(max_length=30) 

    def __str__(self):
        return self.first_name