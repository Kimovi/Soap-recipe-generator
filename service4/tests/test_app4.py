from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class Testbenefit(TestBase):
    def test_honey(self):
        response = self.client.post(url_for('benefit'), data = "Honey",)
        self.assertIn(b'help lighten skin, and reduce wrinkles.', response.data)
    
    def test_coffee(self):
        response = self.client.post(url_for('benefit'), data = "Coffee",)
        self.assertIn(b'leaving your skin looking fresh and feeling smooth. Caffeine may also have the benefits of reducing the effects of cellulite and offering a more neutral tone for the skin.', response.data)
    
    def test_greenTea(self):
        response = self.client.post(url_for('benefit'), data = "Green tea",)
        self.assertIn(b'Green tea contains several vitamins, including vitamin E, which is known for its ability to nourish and hydrate the skin.', response.data)
    
    def test_Lavender(self):
        response = self.client.post(url_for('benefit'), data = "Lavender",)
        self.assertIn(b'help lighten skin, and reduce wrinkles.', response.data)

    def test_Orange(self):
        response = self.client.post(url_for('benefit'), data = "Orange",)
        self.assertIn(b'Antioxidants found in Oranges will brighten your skin', response.data)

    def test_avocado(self):
        response = self.client.post(url_for('benefit'), data = "Avocado butter",)
        self.assertIn(b'Smooths wrinkles and prevents skin aging.', response.data)
        