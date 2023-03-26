import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


def request(session):
    try:
        session.get("http://localhost:8083/status/104")
    except Exception as e:
        print(type(e))
        print(e)


def using_requests_adapters():
    session = requests.Session()

    session.mount("https://", HTTPAdapter(max_retries=5))
    session.mount("http://", HTTPAdapter(max_retries=5))

    request(session)


def using_urllin3_retry():
    session = requests.Session()
    adapter = HTTPAdapter(
        max_retries=Retry(total=4, backoff_factor=1, allowed_methods=None, status_forcelist=[104, 107, 109]))
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    request(session)


USE_URLLIB3 = True
if __name__ == "__main__":
    if USE_URLLIB3:
        using_urllin3_retry()
    else:
        using_requests_adapters()
