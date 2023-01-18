from aiohttp import web
from schemas import EncodeRequestModel
from core import (
    encode_to_percent,
    encode_to_punycode,
    encode_to_base64
)


__all__ = ('routes',)
routes = web.RouteTableDef()


@routes.get('/percent', name='percent')
async def encode_to_unicode_handler(request: web.Request):
    query = dict(EncodeRequestModel(**request.query))
    url = encode_to_percent(query.get('url'))
    return web.Response(body=url)


@routes.get('/punycode', name='punycode')
async def encode_to_unicode_handler(request: web.Request):
    query = dict(EncodeRequestModel(**request.query))
    url = encode_to_punycode(query.get('url'))
    return web.Response(body=url)


@routes.get('/base64', name='base64')
async def encode_to_base64_handler(request: web.Request):
    query = dict(EncodeRequestModel(**request.query))
    url = encode_to_base64(query.get('url'))
    return web.Response(body=url)
