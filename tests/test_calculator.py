import pytest
from fastapi.testclient import TestClient

from calculator import addition, division, multiplication, subtraction
from main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (-1, 1, 0), (0, 0, 0), (2.5, 2.5, 5)])
def test_addition(a, b, expected):
    assert addition(a, b) == expected

def test_subtraction():
    assert subtraction(5, 3) == 2
    assert subtraction(10, 7) == 3


def test_multiplication():
    assert multiplication(3, 4) == 12
    assert multiplication(-2, 5) == -10


def test_division():
    assert division(10, 4) == 2.5
    assert division(1, 3) == 0.33
    assert division(5, 0) == "division by zero not permissible"


def test_root_api(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "app is running"}


@pytest.mark.parametrize(
    "endpoint, params, expected",
    [
        ("/add", {"a": 5, "b": 3}, {"result": 8}),
        ("/sub", {"a": 5, "b": 3}, {"result": 2}),
        ("/mul", {"a": 5, "b": 3}, {"result": 15}),
        ("/div", {"a": 10, "b": 4}, {"result": "2.50"}),
    ],
)
def test_calculator_api_operations(client, endpoint, params, expected):
    response = client.get(endpoint, params=params)

    assert response.status_code == 200
    assert response.json() == expected


@pytest.mark.parametrize(
    "params",
    [
        {"a": 5},
        {"a": "not-a-number", "b": 3},
    ],
)
def test_calculator_api_rejects_invalid_query_params(client, params):
    response = client.get("/add", params=params)

    assert response.status_code == 422
