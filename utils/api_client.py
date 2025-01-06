import requests


class ApiClient:
    def __init__(self, base_url, auth=None):
        """
        Initialize the API client.

        :param base_url: Base URL for the API.
        :param auth: Optional authentication (e.g., token or tuple for Basic Auth).
        """
        self.base_url = base_url
        self.auth = auth

    def _get_headers(self):
        """
        Generate request headers, including authorization if provided.
        """
        headers = {"Content-Type": "application/json"}
        if isinstance(self.auth, str):  # Token-based authentication
            headers["Authorization"] = f"Bearer {self.auth}"
        return headers

    def get(self, endpoint, params=None):
        """
        Perform a GET request.

        :param endpoint: API endpoint.
        :param params: Query parameters.
        :return: JSON response.
        """
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data=None):
        """
        Perform a POST request.

        :param endpoint: API endpoint.
        :param data: Request payload.
        :return: JSON response.
        """
        response = requests.post(f"{self.base_url}/{endpoint}", headers=self._get_headers(), json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint):
        """
        Perform a DELETE request.

        :param endpoint: API endpoint.
        :return: HTTP status code.
        """
        response = requests.delete(f"{self.base_url}/{endpoint}", headers=self._get_headers())
        response.raise_for_status()
        return response.status_code
