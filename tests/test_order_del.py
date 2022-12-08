import pytest

from django.contrib.auth.models import User
from django.test import Client

from booking.models import Order
from booking.models import Rooms


@pytest.mark.django_db
class TestOrderDel:
    def test_order_del(self):
        client = Client()

        user = User.objects.create(
            username="test", email="test@test.com", password="test"
        )
        Order.objects.create(user=user, date_come="2022-4-3", date_out="2022-5-3", count=3)
        room = Rooms.objects.create(title="Test", cost=100)

        client.force_login(user)

        response = client.post(f"/add/{room.id}")
        assert response.status_code == 302

        response = client.get("/order/")
        assert response.status_code == 200

        response = client.get(f"/remove/{room.id}")
        assert response.status_code == 302
