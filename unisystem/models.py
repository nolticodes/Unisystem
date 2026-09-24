from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Studentenausweis(models.Model):
    student = models.OneToOneField("Student", on_delete=models.CASCADE)
    ausweisnummer = models.CharField(max_length=20, unique=True)

class Professor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Kurs(models.Model):
    kurs_name = models.CharField(max_length=50)
    studenten = models.ManyToManyField("Student")
    kurs_professor = models.ForeignKey("Professor", on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey("Semester", on_delete=models.PROTECT,
    )

class Kursbeschreibung(models.Model):
    beschreibung = models.TextField()
    kurs = models.OneToOneField("Kurs", on_delete=models.CASCADE)

class Semester(models.Model):
    semester = models.CharField(max_length=30)
