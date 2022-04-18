from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from first_app.models import Student
from common.serializers import CustomSerializer
from first_app.serializers import se
from common.apis import FullViewSet
class List(FullViewSet):

    ObjModel = Student
    ObjSerializer = se
    print("hello")
    def obj_filter(self, request):

        return self.ObjModel.objects.all()