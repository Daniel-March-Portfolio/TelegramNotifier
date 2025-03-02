from django.urls import path

from blank.views import SendAPIView, UpdateAPIView

urlpatterns = [
    path('send/', SendAPIView.as_view()),
    path('update/', UpdateAPIView.as_view()),
]
