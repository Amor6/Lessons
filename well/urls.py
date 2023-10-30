from django.urls import path, include
from rest_framework.routers import DefaultRouter
from well.views import CourseViewSet, LessonListCreateView, LessonRetrieveUpdateDestroyView, PaymentListView

router = DefaultRouter()
router.register(r'well', CourseViewSet)

app_name = 'well'

urlpatterns = [
    path('', include(router.urls)),
    path('lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroyView.as_view(), name='lesson-retrieve-update-destroy'),
    path('payments/', PaymentListView.as_view(), name='payment-list'),
]