from django.test import TestCase

from taxi.models import Manufacturer


class ManufacturerModelTests(TestCase):
    name_manufacturer = "test"
    country_manufacturer = "Germany"

    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(
            name=self.name_manufacturer, country=self.country_manufacturer
        )
        self.assertEqual(
            str(manufacturer),
            f"{self.name_manufacturer} {self.country_manufacturer}"
        )

    def test_ordering_manufacturers(self):
        Manufacturer.objects.create(name="BMW", country="Germany")
        Manufacturer.objects.create(name="Audi", country="Germany")
        Manufacturer.objects.create(name="Tesla", country="USA")

        manufacturers = Manufacturer.objects.all()
        names = [manufacturer.name for manufacturer in manufacturers]

        self.assertEqual(names, ["Audi", "BMW", "Tesla"])
