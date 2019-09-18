from django.db import models



class Student(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    contact=models.IntegerField()
    emial=models.EmailField(max_length=50)
    age=models.IntegerField()

    class Meta:
        db_table='student'



class Emp(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    forget=models.CharField(max_length=50)

    class Meta:
        db_table='Emp'




