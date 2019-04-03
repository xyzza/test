import asyncio

from aiohttp import web


async def counter(request):

    pool = request.app["db"]
    async with pool.acquire() as connection:
        async with connection.cursor() as cursor:
            await asyncio.shield(
                cursor.execute(
                    """
                    WITH current AS (SELECT req FROM counter FOR UPDATE)
                    UPDATE counter
                    SET req = (SELECT current.req +1 FROM current)
                    RETURNING req;
                    """
                )
            )
            result = await cursor.fetchone()

    return web.Response(text=str(result[0]))
