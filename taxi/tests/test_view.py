from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from taxi.models import Car, Manufacturer


class CarListViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpass123",
        )
        self.client.login(username="testuser", password="testpass123")

        manufacturer = Manufacturer.objects.create(
            name="BMW",
            country="Germany",
        )
        self.car1 = Car.objects.create(model="X5", manufacturer=manufacturer)
        self.car2 = Car.objects.create(model="M3", manufacturer=manufacturer)
        self.car3 = Car.objects.create(model="i8", manufacturer=manufacturer)

    def test_car_list_view_returns_all_cars(self):
        url = reverse("taxi:car-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.car1.model)
        self.assertContains(response, self.car2.model)
        self.assertContains(response, self.car3.model)

    def test_car_list_view_search_by_model(self):
        url = reverse("taxi:car-list")
        response = self.client.get(url, {"model": "M3"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.car2.model)
        self.assertNotContains(response, self.car1.model)
        self.assertNotContains(response, self.car3.model)
