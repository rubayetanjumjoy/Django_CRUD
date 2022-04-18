import json
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from first_app.models import Student
from common.serializers import CustomSerializer


class se(CustomSerializer):

    class Meta:
        model = Student
        fields = '__all__'