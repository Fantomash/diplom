import requests


class ApiUtils:

    def make_post_request(api_url, queries=None, payload=None):
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, params=queries, json=payload, headers=headers)
        return response
