from django.urls import path,include
from .views import SongsView,DockerContainer

urlpatterns = [
    path('api/version/',SongsView.as_view()),
    path('api/version/<int:pk>',SongsView.as_view()),
    path('status/<int:pk>',DockerContainer.as_view()),
    path('run/<int:pk>',DockerContainer.as_view()),
]