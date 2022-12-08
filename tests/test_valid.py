import re
import pytest
import random

from faker import Faker
from django.contrib.auth.models import User

faker = Faker()


class ValidationError(Exception):
    """Raises when password is not valid."""


# Проверяет наличие символов в обоих регистрах,
# чисел, спецсимволов и минимальную длину 10 символов
pattern1 = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{10,}$'

# Проверяет наличие символов в обоих регистрах,
# числел и минимальную длину 10 символов
pattern2 = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{10,}$'


def validate_by_regexp(password, pattern):
    """Валидация пароля по регулярному выражению."""
    if re.match(pattern, password) is None:
        raise ValidationError('Password has incorrecr format.')


@pytest.mark.django_db
def test_validate_by_regexp():
    pas1 = ''
    pas2 = ''
    for x in range(10):  # Количество символов (10)
        pas1 = pas1 + random.choice(list('123xwzXWZ@$!%*#?&'))
        pas2 = pas2 + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

    data_1 = {
        "email": faker.email(),
        "password": pas1,
    }
    data_2 = {
        "email": faker.email(),
        "password": pas2,
    }
    user_1 = User.objects.create(username="Test1", email=data_1["email"], password=data_1["password"])
    user_2 = User.objects.create(username="Test2", email=data_2["email"], password=data_2["password"])

    password1 = user_1.password
    password2 = user_2.password

    assert validate_by_regexp(password1, pattern1) is None
    with pytest.raises(ValidationError):
        validate_by_regexp(password2, pattern1)
    assert validate_by_regexp(password2, pattern2) is None


