from .models import Studentmodel, Markmodel
from .serializers import Studentserializer, Marksserializer
from rest_framework import viewsets

class Studentapi(viewsets.ModelViewSet):
    queryset = Studentmodel.objects.all()
    serializer_class = Studentserializer

class Marksapi(viewsets.ModelViewSet):
    queryset = Markmodel.objects.all()
    serializer_class = Marksserializer