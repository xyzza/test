import asyncio
from functools import partial

import uvloop
from aiohttp import web

from .db import init_db
from .settings import DB_DSN
from .settings import DB_POOLSIZE
from .settings import DB_TIMEOUT
from .view import counter as counter_view


async def on_startup(loop, app):
    app["db"] = await init_db(DB_DSN, DB_POOLSIZE, DB_TIMEOUT, loop)


async def on_cleanup(app):
    app["db"].close()


def run_app():

    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)

    app = web.Application(loop=loop)

    app.on_startup.append(partial(on_startup, loop))
    app.on_cleanup.append(on_cleanup)

    app.add_routes([web.get("/", counter_view)])

    web.run_app(app)
