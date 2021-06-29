from rest_framework import serializers
from student.models import Studentmodel, Markmodel

class Marksserializer(serializers.ModelSerializer):
    class Meta:
        model = Markmodel
        fields = "__all__"

class Studentserializer(serializers.ModelSerializer):
    marks=Marksserializer(read_only=True, many=True)
    class Meta:
        model = Studentmodel
        fields = "__all__"

