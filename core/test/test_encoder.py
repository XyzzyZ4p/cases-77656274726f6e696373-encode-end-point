import pytest
from core.encoder import (
    encode_to_percent,
    encode_to_punycode,
    encode_to_base64
)


@pytest.mark.parametrize('name, value',
                         [('https://гибдд.рф',
                           'https://%D0%B3%D0%B8%D0%'
                           'B1%D0%B4%D0%B4.%D1%80%D1%84')]
)
def test_encode_to_percent(name, value):
    assert value == encode_to_percent(name)


@pytest.mark.parametrize('name, value',
                         [('https://гибдд.рф',
                           'https://xn--90adear.xn--p1ai')])
def test_encode_to_punycode(name, value):
    assert value == encode_to_punycode(name)


@pytest.mark.parametrize('name, value',
                         [('https://гибдд.рф',
                           'aHR0cHM6Ly/Qs9C40LHQtNC0LtGA0YQ=')])
def test_encode_to_punycode(name, value):
    assert value == encode_to_base64(name)
