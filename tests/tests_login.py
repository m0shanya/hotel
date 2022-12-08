import pytest

from faker import Faker
from django.test import Client
from django.contrib.auth.models import User

faker = Faker()


@pytest.mark.django_db
class Test:
    def test_register(self):
        client = Client()

        data = {
            "email": faker.email(),
            "password": faker.password(),
        }
        user = User.objects.create(username="Test", email=data["email"], password=data["password"], first_name="test",
                                   last_name="test")

        response = client.post("/register/", data=data)
        assert response.status_code == 200

        response = client.post("/login/", data=data)
        assert response.status_code == 200

        response = client.post("/logout/")
        assert response.status_code == 200
