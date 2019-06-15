from django.urls import path,include
from .views import SongsView

urlpatterns = [
    path('api/version/',SongsView.as_view()),
    path('api/version/<int:pk>',SongsView.as_view()),
]