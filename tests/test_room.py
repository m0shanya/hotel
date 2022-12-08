import pytest

from django.contrib.auth.models import User
from django.test import Client
from booking.models import Rooms


@pytest.mark.django_db
class TestRoom:
    def test_rooms(self):
        client = Client()

        user = User.objects.create(
            username="test", email="test@test.com", password="test"
        )
        room = Rooms.objects.create(title="Test", cost=100)

        client.force_login(user)

        response = client.get(f"/product/{room.id}/")
        assert response.status_code == 200
