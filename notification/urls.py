from django.urls import path

from notification.views import NotifyAPIView

urlpatterns = [
    path('notify/', NotifyAPIView.as_view()),
]
