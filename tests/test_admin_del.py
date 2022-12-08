from booking.models import Rooms
import pytest
from django.test import Client

from django.contrib.auth.models import User


@pytest.mark.django_db
class TestAdminDel:
    def test_admin_delete(self):
        client = Client()
        user = User.objects.create(
            username="test",
            first_name="test",
            last_name="test",
            email="test@test.com",
            password="test",
            is_staff=True
        )
        client.login(username=user.username, password=user.password)
        response = client.post('/login/', username=user.username, password=user.password)
        assert response.status_code == 200

        response = client.get('/admin/booking/rooms/')
        assert response.status_code == 302
        assert Rooms.objects.count() == 0

        room = Rooms.objects.create(title="Test", cost=100)
        assert Rooms.objects.count() == 1

        response = client.post(f"/admin/booking/rooms/{room.id}/delete/", Rooms.objects.filter(id=room.id).delete()[1])
        assert response.status_code == 302
        assert Rooms.objects.count() == 0
