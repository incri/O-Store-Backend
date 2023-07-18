from store.models import Collection, Product
from model_bakery import baker

from rest_framework import status
import pytest


@pytest.fixture
def create_product(api_client):
    def do_create_product(product):
        return api_client.post("/store/products/", product)

    return do_create_product


@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_anonymous_return_401(self, create_product):
        response = create_product({"title": "a"})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_return_403(self, create_product, authenticate_user):
        authenticate_user()
        response = create_product({"title": "a"})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_return_400(self, create_product, authenticate_user):
        authenticate_user(is_staff=True)
        response = create_product({"title": ""})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_data_is_valid_return_201(self, create_product, authenticate_user):
        authenticate_user(is_staff=True)
        collection = baker.make(Collection)
        response = create_product(
            {
                "title": "Chowmin",
                "description": "good quality food",
                "price": 400.0,
                "price_with_tax": 440.00000000000006,
                "inventory": 21,
                "slug": "chowmin",
                "collection": collection.id,
            }
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] > 0

@pytest.mark.django_db
class TestRetrieveProduct:
    def test_if_collection_exist_return_200(api_client):

        collection = baker.make(Collection)
        product = baker.make(Product, collection = collection)

        response = api_client.get(f"/store/products/{product.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {"id": product.id}

