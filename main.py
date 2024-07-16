import requests

def make_api_call(url, headers=None, params=None):
    """
    Makes an API call to the specified URL with optional headers and parameters.

    :param url: The API endpoint URL.
    :param headers: Optional dictionary of HTTP headers to send with the request.
    :param params: Optional dictionary of query parameters to send with the request.
    :return: The response JSON.
    """
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making API call: {e}")
        return None

if __name__ == "__main__":
    api_url = "https://www.marketsmojo.com/portfolio-plus/stickeyheader"
    # api_headers = {
    #     "Accept": "application/json",
    # }
    # api_params = {
    #     "param1": "value1",
    #     "param2": "value2"
    # }

    # response = make_api_call(api_url, headers=api_headers, params=api_params)
    response = make_api_call(api_url)

    if response:
        print("API Response:")
        print(response)
