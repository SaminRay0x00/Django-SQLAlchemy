from django.db import models


class Student(models.Model):


    Name = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)






