from rest_framework import generics, viewsets
from .models import User
from .serializers import UserSerializer, SubscriptionSerializer

from user.models import Subscription





class UserViewSet(viewsets.ModelViewSet):
    """Отображение пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateAPIView(generics.CreateAPIView):
    """Создание пользователей"""
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    """Отображение пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """Обновление пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """Удаление пользователей"""
    queryset = User.objects.all()


class SubscriptionCreateAPIView(generics.CreateAPIView):
    """Создание подписки"""
    serializer_class = SubscriptionSerializer


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    """Удаление подписки"""
    queryset = Subscription.objects.all()
