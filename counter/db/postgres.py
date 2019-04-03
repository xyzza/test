from aiopg import create_pool


async def init_db(dsn, pool_size, timeout, loop):
    return await create_pool(dsn, maxsize=pool_size, loop=loop, timeout=timeout)
