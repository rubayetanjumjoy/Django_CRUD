from django.db import models
from common.models import TSFieldsIndexed
# Create your models here.
class Student(TSFieldsIndexed):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return self.pk