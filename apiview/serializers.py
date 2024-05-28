from .models import Category,MusicKlip
from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    class Meta:
        model = Category
        fields = '__all__'


class MusicKlipSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=100)
    image = serializers.ImageField()
    video = serializers.FileField()
    audio = serializers.FileField()
    docPDF = serializers.FileField()

    class Meta:
        model = MusicKlip
        fields = '__all__'




