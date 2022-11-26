from django.urls import path
from .views import PostApiView

# api url

urlpatterns = [
    path('', PostApiView.as_view(), name='post_api')
]
