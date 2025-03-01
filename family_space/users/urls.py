from django.urls import path
from .views import UserRegisterView, UserLoginView, UserAuthView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('authorization/', UserAuthView.as_view(), name='user-auth'),
]
