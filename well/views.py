from rest_framework import viewsets, generics, filters
from rest_framework.pagination import PageNumberPagination

from .models import Course, Lesson, Payment
from .serializers import CourseSerializer, LessonSerializer, PaymentSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10  # Количество объектов на одной странице
    page_size_query_param = 'page_size'
    max_page_size = 100


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['payment_date']
    pagination_class = CustomPagination


