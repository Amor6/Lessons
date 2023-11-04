from django.urls import path, include
from rest_framework.routers import DefaultRouter
from well.views import CourseViewSet, LessonListCreateView, LessonRetrieveUpdateDestroyView, PaymentListView

from user.views import  SubscriptionCreateAPIView, SubscriptionDestroyAPIView

router = DefaultRouter()
router.register(r'well', CourseViewSet)

app_name = 'well'

urlpatterns = [
    path('', include(router.urls)),
    path('lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroyView.as_view(), name='lesson-retrieve-update-destroy'),
    path('payments/', PaymentListView.as_view(), name='payment-list'),
    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_delete'),
]