from django.urls import path

from blank.views import SendAPIView

urlpatterns = [
    path('send/', SendAPIView.as_view()),
]
