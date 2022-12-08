import pytest

from django.contrib.auth.models import User
from django.test import Client

from booking.models import Order


@pytest.mark.django_db
class TestOrder:
    def test_order(self):
        client = Client()

        user = User.objects.create(
            username="test", email="test@test.com", password="test"
        )
        Order.objects.create(user=user, date_come="2022-4-3", date_out="2022-5-3", count=3)

        client.force_login(user)

        response = client.get("/order/")
        assert response.status_code == 200
