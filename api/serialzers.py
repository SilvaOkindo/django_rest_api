from blog.models import Post
from rest_framework import serializers


# api serializers

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
