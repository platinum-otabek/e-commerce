from django.urls import path

from app.views import CustomUserView

urlpatterns = [
    path('getCustomUsers/', CustomUserView.as_view())
]
