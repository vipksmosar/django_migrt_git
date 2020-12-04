from django.db import models

# Create your models here.

from django.urls import reverse
import uuid


class Salary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="UUID")
    title = models.CharField(max_length=1000, help_text="Description")
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)
    issued = models.FloatField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('salary_detail', args=[str(self.id)])

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    back_name = models.CharField(max_length=100)


    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('employee_detail', args=[str(self.id)])


class Test(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    back_name = models.CharField(max_length=100)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('employee_detail', args=[str(self.id)])