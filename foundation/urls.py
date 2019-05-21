from django.urls import path
from .views import BasePageViewer

urlpatterns = [
    path('', BasePageViewer.as_view()),
]

