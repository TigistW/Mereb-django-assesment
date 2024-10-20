from django.urls import path
from .views import RegisterView, UserView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/<int:pk>/', UserView.as_view(), name='user'),
]
