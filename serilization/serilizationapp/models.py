from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField()
    address = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name
