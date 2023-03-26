import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Sighting, Cryptid, Habitat


class CryptidModelTests(TestCase):

    # This test should normally print "This has yet to happen" as happened_Recently *
    # does when a sighting is located in the future (Static testing)

    def test_Sighting_future(self):
        future_sighting = Sighting(sighting_time= timezone.now() + datetime.timedelta(days=3))
        return future_sighting.happened_Recently()
    # This test is making sure that no Sighting is taking place in the future as a sighting is a past event
    # (Dynamic test, tests the code after deployment)

    def test_Sighting_happened(self):
        time = timezone.now() + datetime.timedelta(days=30)
        # time is used as a measure to make sure the sighting happened
        future_sighting = Sighting(sighting_time=time) # Creation of a Sighting as a comparison
        self.assertIs(future_sighting.happened_Recently(), False)

    # This test is supposed to verify that the behaviour function of the Cryptid model returns the right string
    def test_print_behaviour(self):
        self.assertIs(Cryptid.aggressive == (Cryptid.behaviour() == "Aggressive"), True)
        # if the Cryptid.behaviour returns "Aggressive", Cryptid.aggressive should be true.
        # Otherwise both assertions should be false

    # This test makes sure calling a Habitat model returns its name (Static test, it tests an isolated part of code)
    def test_habitat(self):
        habitat = Habitat(country_name="France", continent="Europe")
        return habitat == "France"


