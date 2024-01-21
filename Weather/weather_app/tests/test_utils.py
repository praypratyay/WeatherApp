import unittest
from weather_app.utils import get_qualitative_name

class TestGetQualitativeName(unittest.TestCase):
    def test_valid_pollutant(self):
        self.assertEqual(get_qualitative_name('so2', 15), "Good")
        self.assertEqual(get_qualitative_name('no2', 45), "Fair")
        self.assertEqual(get_qualitative_name('pm10', 55), "Moderate")
        self.assertEqual(get_qualitative_name('pm2_5', 5), "Good")
        self.assertEqual(get_qualitative_name('o3', 70), "Fair")
        self.assertEqual(get_qualitative_name('co', 5000), "Fair")

    def test_invalid_pollutant(self):
        self.assertEqual(get_qualitative_name('invalid_pollutant', 25), "N/A")

    def test_concentration_below_range(self):
        self.assertEqual(get_qualitative_name('so2', -5), "N/A")

    def test_concentration_above_range(self):
        self.assertEqual(get_qualitative_name('no2', 250), "Very Poor")

    def test_edge_cases(self):
        self.assertEqual(get_qualitative_name('pm10', 20), "Fair")
        self.assertEqual(get_qualitative_name('o3', 60), "Fair")

