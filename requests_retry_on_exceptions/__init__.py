__all__ = ['delete', 'get', 'head', 'options',
           'patch', 'post', 'put', 'request']

import http
import urllib3
import ssl
import time

import requests

BACKOFF_FACTOR = 0.1
EXCEPTIONS = (
    http.client.IncompleteRead,
    requests.exceptions.ChunkedEncodingError,
    requests.exceptions.ConnectionError,
    requests.exceptions.HTTPError,
    requests.exceptions.ReadTimeout,
    requests.exceptions.SSLError,
    requests.exceptions.TooManyRedirects,
    ssl.SSLEOFError,
    urllib3.exceptions.MaxRetryError,
    urllib3.exceptions.ProtocolError,
    urllib3.exceptions.ReadTimeoutError,
)
RETRIES = 3


class Retry:
    backoff_factor = None
    func = None
    exceptions = None
    retries = None

    def __init__(self, func, **kwargs):
        self.func = func
        self.backoff_factor = kwargs.get('backoff_factor', BACKOFF_FACTOR)
        self.exceptions = kwargs.get('exceptions', EXCEPTIONS)
        self.retries = kwargs.get('retries', RETRIES)

    def run(self, *args, **kwargs):
        for key in ['backoff_factor', 'exceptions', 'retries']:
            if key in kwargs:
                del kwargs[key]
        sleep = self.backoff_factor
        retries_count = 0
        while retries_count < self.retries:
            try:
                return self.func(*args, **kwargs)
            except self.exceptions:
                time.sleep(sleep)
                retries_count += 1
                sleep += self.backoff_factor
        return self.func(*args, **kwargs)


def delete(*args, **kwargs):
    return Retry(requests.delete, **kwargs).run(*args, **kwargs)


def get(*args, **kwargs):
    return Retry(requests.get, **kwargs).run(*args, **kwargs)


def head(*args, **kwargs):
    return Retry(requests.head, **kwargs).run(*args, **kwargs)


def options(*args, **kwargs):
    return Retry(requests.options, **kwargs).run(*args, **kwargs)


def patch(*args, **kwargs):
    return Retry(requests.patch, **kwargs).run(*args, **kwargs)


def put(*args, **kwargs):
    return Retry(requests.put, **kwargs).run(*args, **kwargs)


def post(*args, **kwargs):
    return Retry(requests.post, **kwargs).run(*args, **kwargs)


def request(*args, **kwargs):
    return Retry(requests.request, **kwargs).run(*args, **kwargs)
