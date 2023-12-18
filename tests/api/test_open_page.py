import allure
import requests

from helpers.api_utils import ApiUtils
from elements.endpoints import Endpoints


# 9
@allure.feature("API tests")
def test_open_page():
    request = requests.get(Endpoints.PORTAL_URL)
    assert request.status_code == 200


# 10
@allure.feature("API tests")
def test_search_for_accommodation():
    response = ApiUtils.make_post_request(Endpoints.SEARCH_URL,
                                          queries=Endpoints.search_queries_data,
                                          payload=Endpoints.search_payload_data)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert "data" in response.json(), "Field 'data' is not present in the response"
