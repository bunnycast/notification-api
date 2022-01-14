import time
import typing

from starlette.datastructures import Headers
from starlette.requests import Request
from starlette.types import ASGIApp, Scope, Receive, Send

from app.utils.date_utils import D


class AccessControl:
    def __init__(
            self,
            app: ASGIApp,
            except_path_list: typing.Sequence[str] = None,
            except_path_regex: str = None,
    ) -> None:
        if except_path_list is None:
            except_path_list = ["*"]
        self.app = app
        self.except_path_list = except_path_list
        self.except_path_regex = except_path_regex

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        print(self.except_path_regex)
        print(self.except_path_list)

        request = Request(scope=scope)
        headers = Headers(scope=scope)

        request.state.req_time = D.datetime()
        print(D.datetime())
        print(D.date())
        print(D.date_num())
        request.state.start = time.time()
        request.state.inspect = None
        request.state.user = None
        request.state.is_admin_access = None
        print(request.cookies)
        print(headers)
        res = await self.app(scope, receive, send)
        return res
