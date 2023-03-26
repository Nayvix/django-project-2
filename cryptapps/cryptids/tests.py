import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Sighting

class CryptidModelTests(TestCase):

    def test_Sighting_happened(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_sighting = Sighting(sighting_time=time)
        self.assertIs(future_sighting.happened_Recently(), False)

# All the tests were conducted manually, so no test to be seen here
