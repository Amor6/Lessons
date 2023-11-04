from rest_framework import viewsets, generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from well.permissions import IsOwnerOrStaff, IsModerator, IsOwner
from user.models import User, Subscription

from .models import Course, Lesson, Payment
from .serializers import CourseSerializer, LessonSerializer, PaymentSerializer, SubscriptionSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10  # Количество объектов на одной странице
    page_size_query_param = 'page_size'
    max_page_size = 100


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]



class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrStaff, IsModerator]

class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['payment_date']
    pagination_class = CustomPagination

class SubscriptionCreateAPIView(generics.CreateAPIView):
    """Создание подписки"""
    serializer_class = SubscriptionSerializer

class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    """Удаление подписки"""
    queryset = Subscription.objects.all()



