from .engine import engine_dispose


async def close_connections():
    await engine_dispose()
