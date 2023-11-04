from rest_framework import serializers
from .models import User, Subscription

from user.validators import AlreadySubscribedCheck


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        validators = [AlreadySubscribedCheck()]