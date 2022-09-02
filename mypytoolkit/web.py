"""
Web-related actions, including link-shortening, etc.
"""
import requests


def bitly(long_link: str, access_token: str) -> str:
    """Shortens link using the Bitly API. A valid access token is required."""
    if not isinstance(long_link, str):
        raise Exception("You must provide a string.")

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    data = ' {"long_url": "' + long_link + '" } '
    
    response = requests.post(url="https://api-ssl.bitly.com/v4/shorten", headers=headers, data=data)
    return response.json()['link']
