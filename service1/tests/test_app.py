from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app, db
from application.models import Soap

class TestBase(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Soap(mainIngredient = "Honey", oilIngredient = "Avocado oil", benefit = "help lighten skin, and reduce wrinkles."))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestGenerator(TestBase):
    def test_gen(self):
        response = self.client.get(url_for('gen'))
        self.assertEqual(response.status_code, 500)

class TestResponse(TestBase):
    def test_index(self):
        with requests_mock.mock() as g:
            g.get("http://service2/mainIngredient", text = "Honey")
            g.get("http://service3/oilIngredient", text = "Avocado oil")
            g.post("http://service4/benefit", text = "help lighten skin, and reduce wrinkles.")

            response = self.client.get(url_for('gen'))
            self.assertNotIn(b"Honey", response.data)
            self.assertIn(b"Avocado oil", response.data)
            self.assertIn(b"help lighten skin, and reduce wrinkles.", response.data)