from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from well.models import Course, Lesson
from user.models import User
from well.models import Subscription

class SubscriptionPositiveTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@test.com',
        )
        self.user.set_password('test')
        self.user.save()

        self.course = Course.objects.create(
            title='test course',
            description='test course description',
        )

        self.lesson = Lesson.objects.create(
            title='test lesson',
            description='test lesson description',
            video_url='https://www.youtube.com',
            owner=self.user,
            course=self.course,
        )

    def test_subscription_create(self):
        self.client.force_authenticate(user=self.user)

        data = {
            'course': self.course.pk,
            'user': self.user.pk,
        }

        response = self.client.post(
            reverse('users:subscription'),
            data=data,
        )

        # print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('course'), self.course.pk)
        self.assertEqual(response.json().get('user'), self.user.pk)

    def test_subscription_delete(self):
        self.client.force_authenticate(user=self.user)

        subscription = Subscription.objects.create(
            course=self.course,
            user=self.user,
        )

        response = self.client.delete(
            f'user/{subscription.id}/unsubscribe/',
        )

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT,
        )
        self.assertFalse(
            Subscription.objects.all().exists(),
        )


class SubscriptionNegativeTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@test.com',
        )
        self.user.set_password('test')
        self.user.save()

        self.course = Course.objects.create(
            title='test course',
            description='test course description',
        )

        self.lesson = Lesson.objects.create(
            title='test',
            description='test description',
            video_url='https://www.youtube.com',
            owner=self.user,
            course=self.course,
        )
