import typing

import webob
import webtest
from starlette.testclient import TestClient
from starlette.types import ASGIApp


__version__ = "1.0.0"


WSGIApp = typing.Callable[
    [typing.MutableMapping, typing.Callable], typing.List[typing.ByteString]
]


def AsgiToWsgi(asgi_app: ASGIApp) -> WSGIApp:
    def handle(environ, start_response):
        req = webob.Request(environ)
        with TestClient(asgi_app) as client:
            response = client.request(
                method=req.method,
                url=req.path,
                data=req.body,
                params=req.params,
                headers=dict(req.headers),
                cookies=dict(req.cookies),
            )
        res = webob.Response(
            body=response.content,
            status=response.status_code,
            content_type=response.headers.get("content-type"),
            headerlist=list(response.headers.items()),
            charset=response.apparent_encoding,
        )
        start_response(res.status, res.headerlist)
        return res.app_iter

    return handle


class TestApp(webtest.TestApp):
    """A modified `webtest.TestApp` that can wrap an ASGI application. Takes the same
    arguments as `webtest.TestApp`.
    """

    def __init__(self, app: ASGIApp, *args, **kwargs) -> None:
        self.asgi_app = app
        super().__init__(AsgiToWsgi(app), *args, **kwargs)
