import sys
from pathlib import Path
from aiohttp import web
from middlewares import middlewares
from handlers import routes


ROOT = Path(__file__).parents[1]
sys.path.append(str(ROOT))

app = web.Application(middlewares=middlewares)
sub_app = web.Application()
sub_app.add_routes(routes)
app.add_subapp('/encode', sub_app)


if __name__ == '__main__':
    web.run_app(app, host='localhost', port=8080)
