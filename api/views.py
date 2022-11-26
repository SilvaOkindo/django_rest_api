from rest_framework import generics
from blog.models import Post
from .serialzers import PostSerializers


# Create your views here.

class PostApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
