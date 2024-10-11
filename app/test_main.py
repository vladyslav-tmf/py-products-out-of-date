from datetime import date
from unittest.mock import patch

import pytest

from app.main import outdated_products


@pytest.fixture
def sample_products():
    """
    Fixture that provides a sample list of products for testing.
    """
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


@patch('app.main.datetime.date')
def test_outdated_products_today_is_2nd_feb(
    mock_date: patch,
    sample_products: list[dict]
) -> None:
    """
    Test that products expired by 2nd Feb are correctly identified.
    """
    mock_date.today.return_value = date(2022, 2, 2)
    expected = ['duck']
    assert outdated_products(sample_products) == expected, (
        f"Expected {expected}, but got {outdated_products(sample_products)} "
        f"for date {mock_date.today.return_value}"
    )


@patch('app.main.datetime.date')
def test_outdated_products_today_is_6th_feb(
    mock_date: patch,
    sample_products: list[dict]
) -> None:
    """
    Test that products expired by 6th Feb are correctly identified.
    """
    mock_date.today.return_value = date(2022, 2, 6)
    expected = ['chicken', 'duck']
    assert outdated_products(sample_products) == expected, (
        f"Expected {expected}, but got {outdated_products(sample_products)} "
        f"for date {mock_date.today.return_value}"
    )


@patch('app.main.datetime.date')
def test_outdated_products_today_is_11th_feb(
    mock_date: patch,
    sample_products: list[dict]
) -> None:
    """
    Test that products expired by 11th Feb are correctly identified.
    """
    mock_date.today.return_value = date(2022, 2, 11)
    expected = ['salmon', 'chicken', 'duck']
    assert outdated_products(sample_products) == expected, (
        f"Expected {expected}, but got {outdated_products(sample_products)} "
        f"for date {mock_date.today.return_value}"
    )


@patch('app.main.datetime.date')
def test_outdated_products_today_is_1st_feb(
    mock_date: patch,
    sample_products: list[dict]
) -> None:
    """
    Test that no products are expired by 1st Feb.
    """
    mock_date.today.return_value = date(2022, 2, 1)
    expected = []
    assert outdated_products(sample_products) == expected, (
        f"Expected {expected}, but got {outdated_products(sample_products)} "
        f"for date {mock_date.today.return_value}"
    )


def test_outdated_products_empty_list() -> None:
    """
    Test that empty product list returns empty result.
    """
    assert outdated_products([]) == [], (
        "Expected an empty list, but got a non-empty result."
    )
