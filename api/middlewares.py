from pydantic import ValidationError
from aiohttp.web import middleware, HTTPBadRequest


__all__ = ('middlewares',)


@middleware
async def errors_catcher(request, handler):
    try:
        resp = await handler(request)
    except ValidationError:
        raise HTTPBadRequest
    else:
        return resp


middlewares = [errors_catcher]
