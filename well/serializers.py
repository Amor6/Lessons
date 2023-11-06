from rest_framework import serializers
from .models import Course, Lesson, Payment

from models import Subscription
from user.validators import AlreadySubscribedCheck

class CourseSerializer(serializers.ModelSerializer):
    num_lessons = serializers.SerializerMethodField()
    lessons = serializers.StringRelatedField(many=True, read_only=True)  # Поле вывода уроков

    class Meta:
        model = Course
        fields = '__all__'

    def get_num_lessons(self, obj):
        # Вывод уроков
        return obj.lesson_set.count()


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        validators = [AlreadySubscribedCheck()]