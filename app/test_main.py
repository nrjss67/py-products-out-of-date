import pytest
from datetime import date
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def products() -> dict:
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "expiration_date,expected",
    [
        (date(2022, 2, 1), []),
        (date(2022, 2, 2), ["duck"]),
        (date(2022, 2, 5), ["duck"]),
        (date(2022, 2, 6), ["chicken", "duck"]),
        (date(2022, 2, 10), ["chicken", "duck"]),
        (date(2022, 2, 11), ["salmon", "chicken", "duck"])
    ]
)
@mock.patch("app.main.datetime.date")
def test_with_expired_date(mocked_today, expiration_date, expected, products): # noqa
    mocked_today.today.return_value = expiration_date
    assert outdated_products(products) == expected
