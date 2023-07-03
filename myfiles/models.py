from django.db import models


# Create your models here.
class Kurs(models.Model):
    nomi = models.CharField(max_length=50)
    def __str__(self):
        return self.nomi


class Student(models.Model):
    ism = models.CharField(max_length=40)
    familya = models.CharField(max_length=40)
    yosh = models.IntegerField()
    manzil = models.CharField(max_length=100)
    yonalish = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
