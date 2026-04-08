import requests

def test_status_code():
    url = "https://api.github.com"
    response = requests.get(url)
    assert response.status_code == 200
