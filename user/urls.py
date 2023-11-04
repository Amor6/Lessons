from django.urls import path

from .apps import UserConfig
# from .views import UserListCreateView, UserRetrieveUpdateDestroyView
from user.views import  UserCreateAPIView, UserListAPIView, UserUpdateAPIView, UserDestroyAPIView, \
    SubscriptionCreateAPIView, SubscriptionDestroyAPIView


app_name = UserConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='list_user'),
    path('users/', UserCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserUpdateAPIView.as_view(), name='user-retrieve-update-destroy'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='delete_user'),
    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_delete'),

]

