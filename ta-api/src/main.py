from typing import Awaitable, Callable

from fastapi import FastAPI, Request, Response, status
from mangum import Mangum
from starlette.middleware.base import BaseHTTPMiddleware

from ta_api.routers import account, admin, auth, event, verify

app = FastAPI()


class CORSMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        if request.method == "OPTIONS":
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            return await call_next(request)


app.add_middleware(CORSMiddleware)

app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
)

app.include_router(
    account.router,
    prefix="/accounts",
    tags=["accounts"],
)

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    verify.router,
    prefix="/verify",
    tags=["verify"],
)

app.include_router(
    event.router,
    prefix="/events",
    tags=["events"],
)

lambda_handler = Mangum(app)
