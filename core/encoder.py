import base64
import idna
from furl import furl
from urllib.parse import urlparse, quote, urlunparse

__all__ = (
    'encode_to_percent',
    'encode_to_punycode',
    'encode_to_base64'
)


def encode_to_percent(url: str):
    url_parts = list(urlparse(url))
    url_parts[1] = quote(url_parts[1], safe='')
    url_parts[4] = quote(url_parts[4], safe='')
    return urlunparse(url_parts)


def encode_to_punycode(url: str):
    url_parts = urlparse(url)
    url_parts._replace(netloc=idna.encode(url_parts.netloc).decode())
    punyfied = str(furl(url_parts.geturl()))
    return punyfied


def encode_to_base64(url: str):
    return base64.b64encode(url.encode('utf-8')).decode('utf-8')
