from typing import Callable

import uvicorn
from fastapi import FastAPI, Response, Request
from fastapi.routing import APIRoute
from mangum import Mangum
from starlette.middleware.exceptions import ExceptionMiddleware
from aws_lambda_powertools import Logger


class LoggerRouteHandler(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def route_handler(request: Request) -> Response:
            # Add fastapi context to logs
            ctx = {
                "path": request.url.path,
                "route": self.path,
                "method": request.method,
                "body": request.scope.get('aws.event', {}).get('body', 'DIRECT_CALL')
            }
            logger.append_keys(fastapi=ctx)
            logger.info("Received request")

            response = await original_route_handler(request)
            ctx["body"] = getattr(response, 'body', '')
            logger.append_keys(fastapi=ctx)
            logger.info("Successfully completed request")

            return response

        return route_handler


app = FastAPI()
app.router.route_class = LoggerRouteHandler
# noinspection PyTypeChecker
app.add_middleware(ExceptionMiddleware, handlers=app.exception_handlers)

logger: Logger = Logger(log_uncaught_exceptions=True)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run("app:handler")
else:
    handler = Mangum(app)
    handler = logger.inject_lambda_context(handler, clear_state=True)