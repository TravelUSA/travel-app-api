from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Itenary

from travel.serializers import ItenarySerializer

ITENARY_URL = reverse('travel:itenary-list')


class PublicItenaryApiTests(TestCase):
    """Test the publicly available itenary apis"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Login is required to access the requirements"""

        res = self.client.get(ITENARY_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateItenaryApiTests(TestCase):
    """Test the private itenary"""

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@travelusa.com',
            'testpass'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_itenary_list(self):
        """ test retrieving a list of itenaries"""
        Itenary.objects.create(user=self.user, name='NJ', travel_time='future', places ='Edison')
        Itenary.objects.create(user=self.user, name='NY', travel_time='next', places ='NYC')

        res = self.client.get(ITENARY_URL)
        itenaries = Itenary.objects.all().order_by('-name')
        serializer = ItenarySerializer(itenaries, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_itenaries_limited_to_user(self):
        """Test the itenaries for authenticated users are returned"""
        user2 = get_user_model().objects.create_user(
            'other@travelusa.com',
            'testpass'
        )
        Itenary.objects.create(user=user2, name='NJ')
        itenary = Itenary.objects.create(user=self.user, name='NY')
        res = self.client.get(ITENARY_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], itenary.name)
