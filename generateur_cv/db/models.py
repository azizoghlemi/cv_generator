from django.db import models
from datetime import date
class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=40, default=None)
    adress = models.CharField(max_length=50, default=None)
    postal = models.CharField(max_length=10, default=None)
    town = models.CharField(max_length=30, default=None)
    phone = models.CharField(max_length=30, default=None)
    mail = models.CharField(max_length=100, default=None)
    nationality = models.CharField(max_length=30, default=None)
    date_of_birth = models.CharField(max_length=30, default=None )
    link = models.CharField(max_length=100, default=None)
    license = models.CharField(max_length=100, default=None)
    profile = models.CharField(max_length=500, default=None)
    picture = models.ImageField(default=None)


    def __str__(self):
        return self.id

class Education(models.Model):

    degree = models.CharField(max_length=30,primary_key=True)
    establishment = models.CharField(max_length=30, default=None)
    town = models.CharField(max_length=30, default=None)
    start = models.CharField(max_length=30,default=None)
    end = models.CharField(max_length=30,default=None)
    description = models.CharField(max_length=300, default=None)

class Training(models.Model):

    training =  models.CharField(max_length=30,primary_key=True)
    establishment = models.CharField(max_length=30, default=None)
    town = models.CharField(max_length=30,default=None)
    start = models.CharField(max_length=30,default=None)
    end = models.CharField(max_length=300,default=None)
    description = models.CharField(max_length=300, default=None)
class Experience(models.Model):

    experience =  models.CharField(max_length=30,primary_key=True )
    establishment = models.CharField(max_length=30, default=None)
    town = models.CharField(max_length=30,default=None)
    start = models.CharField(max_length=30,default=None)
    end = models.CharField(max_length=300,default=None)
    description = models.CharField(max_length=300, default=None)

class Skills(models.Model):

    skill =  models.CharField(max_length=30,primary_key=True)
    level = models.CharField(max_length=2, default=None)

class Languages(models.Model):

    language =  models.CharField(max_length=30,primary_key=True)
    level = models.CharField(max_length=2, default=None)

class Hobbies(models.Model):

    hobbies = models.CharField(max_length=300, default=None)

class Internships(models.Model):

    internship = models.CharField(max_length=40,primary_key=True)
    employer = models.CharField(max_length=30, default=None)
    town = models.CharField(max_length=30,default=None)
    start = models.CharField(max_length=30,default=None)
    end = models.CharField(max_length=300,default=None)
    description = models.CharField(max_length=300, default=None)

class Community(models.Model):

    experience = models.CharField(max_length=30,primary_key=True)
    establishment = models.CharField(max_length=30, default=None)
    town = models.CharField(max_length=30,default=None)
    start = models.CharField(max_length=30,default=None)
    end = models.CharField(max_length=300,default=None)
    description = models.CharField(max_length=300, default=None)

class Certificates(models.Model):

    certificate = models.CharField(max_length=30,primary_key=True)
    period = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=300, default=None)

# Create your models here.
