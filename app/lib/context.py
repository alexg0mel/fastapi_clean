from typing import Annotated
from uuid import uuid4

from fastapi import Request, Depends


async def get_request_id(request: Request) -> str:
    yield request.scope.get('request_id')


async def context_header(request: Request, call_next):
    request.scope.update({'request_id': request.headers.get('X-Request-Id', str(uuid4()))})
    response = await call_next(request)
    response.headers["X-Request-Id"] = request.scope.get('request_id')
    return response


RequestId = Annotated[str, Depends(get_request_id)]
