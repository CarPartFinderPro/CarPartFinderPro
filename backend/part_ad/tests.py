"""
Test Module
"""

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import CarPart


class CarPartTestCase(TestCase):
    """Test case for the CarPart model"""

    def setUp(self):
        """Set up test case"""
        self.client = Client()
        self.car_part = CarPart.objects.create(
            title="Test Car Part",
            brand="Test Brand",
            model="Test Model",
            year_from="2020",
            price=100,
            description="Test Description"
        )

    def test_car_part_details(self):
        """Test the car part details API endpoint"""
        response = self.client.get(reverse('car_part_details', args=[self.car_part.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.car_part.title)
        self.assertEqual(response.data['brand'], self.car_part.brand)

    def test_car_part_detail_view(self):
        """Test the car part detail view API endpoint"""
        response = self.client.get(reverse('car_part_detail_view', args=[self.car_part.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.car_part.title)
        self.assertEqual(response.data['brand'], self.car_part.brand)


class CarPartAPITestCase(APITestCase):
    """Test case for the CarPart API"""

    def setUp(self):
        """Set up test case"""
        self.client = APIClient()
        self.car_part = CarPart.objects.create(
            title="Test Car Part",
            brand="Test Brand",
            model="Test Model",
            year_from="2020",
            price=100,
            description="Test Description"
        )

    def test_car_part_list(self):
        """Test the car part list API endpoint"""
        response = self.client.get(reverse('carpart-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_car_part_create(self):
        """Test the car part create API endpoint"""
        data = {
            "title": "Test Car Part 2",
            "brand": "Test Brand 2",
            "model": "Test Model 2",
            "year_from": "2022",
            "price": 200,
            "description": "Test Description 2"
        }
        response = self.client.post(reverse('carpart-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CarPart.objects.count(), 2)
