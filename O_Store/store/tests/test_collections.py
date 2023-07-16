from django.contrib.auth.models import User

from rest_framework import status
import pytest


@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post("/store/collections/", collection)

    return do_create_collection


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_return_401(self, create_collection):
        # AAA (Arrange, Act, Assert)

        # Arranger

        # Act
        response = create_collection({"title": "a"})

        # Assert

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_return_403(
        self, authenticate_user, create_collection
    ):
        authenticate_user()  # Arranger

        response = create_collection({"title": "a"})  # Act

        assert response.status_code == status.HTTP_403_FORBIDDEN  # Assert

    def test_if_data_is_invalid_return_400(self, authenticate_user, create_collection):
        authenticate_user(is_staff=True)

        response = create_collection({"title": ""})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["title"] is not None

    def test_if_data_is_valid_return_201(self, authenticate_user, create_collection):
        authenticate_user(is_staff=True)

        response = create_collection({"title": "a"})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] > 0
