<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/requests-retry-on-exceptions.svg?maxAge=3600)](https://pypi.org/project/requests-retry-on-exceptions/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/requests-retry-on-exceptions.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/requests-retry-on-exceptions.py/actions)

### Installation
```bash
$ [sudo] pip install requests-retry-on-exceptions
```

#### Features
+   default `backoff_factor`: `0.1`
+   default `retries`: `3`
+   default `exceptions`:
    +   `http.client.IncompleteRead`
    +   `requests.exceptions.ChunkedEncodingError`
    +   `requests.exceptions.ConnectionError`
    +   `requests.exceptions.HTTPError`
    +   `requests.exceptions.ReadTimeout`
    +   `requests.exceptions.SSLError`
    +   `requests.exceptions.TooManyRedirects`
    +   `ssl.SSLEOFError`
    +   `urllib3.exceptions.MaxRetryError`
    +   `urllib3.exceptions.ProtocolError`
    +   `urllib3.exceptions.ReadTimeoutError`

#### Examples
```python
import requests_retry_on_exceptions as requests

r = requests.get('https://pypi.org/project/django/')
```

options:
```python
r = requests.get(url,exceptions=(requests.exceptions.SSLError,),backoff_factor=0.1,retries=3)
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>