from booking.models import Rooms
import pytest
from django.test import Client

from django.contrib.auth.models import User


@pytest.mark.django_db
class TestAdmin:
    def test_admin_create(self):
        client = Client()
        admin_user = User.objects.create(
            username="test",
            first_name="test",
            last_name="test",
            email="test@test.com",
            password="test",
            is_staff=True
        )
        client.login(username=admin_user.username, password=admin_user.password)
        response = client.post('/login/', username=admin_user.username, password=admin_user.password)
        assert response.status_code == 200
        response = client.get('/admin/booking/rooms/')
        assert response.status_code == 302
        assert Rooms.objects.count() == 0
        response = client.post(
            "/admin/booking/rooms/add/",
            {
                "title": "title",
                "slug": "slug",
                "cost": "100",
                "_save": "Save",
            }
        )
        assert response.status_code == 302
