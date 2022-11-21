import typing

import webob
import webtest
from starlette.testclient import TestClient
from starlette.types import ASGIApp


__version__ = "1.1.0"


WSGIApp = typing.Callable[
    [typing.MutableMapping, typing.Callable], typing.List[typing.ByteString]
]


def AsgiToWsgi(asgi_app: ASGIApp) -> WSGIApp:
    def handle(environ, start_response):
        """
        Support logic and avoiding deprecation warnings for httpx-based TestClient
        Starlette (from version >=0.21.0) uses httpx as a base for TestClient's logic
        """
        req = webob.Request(environ)
        with TestClient(asgi_app, cookies=dict(req.cookies)) as client:
            content_kwargs = {}
            # sending raw-bytes content must be through "content" argument
            # avoiding DeprecationWarning: Use 'content=<...>'
            # to upload raw bytes/text content.
            if req.body is not None and not isinstance(req.body, dict):
                content_kwargs["content"] = req.body
            else:
                content_kwargs["data"] = req.body

            response = client.request(
                method=req.method,
                url=req.url,
                headers=dict(req.headers),
                **content_kwargs,
            )

        res = webob.Response(
            body=response.content,
            status=response.status_code,
            content_type=response.headers.get("content-type"),
            headerlist=list(response.headers.items()),
            charset=response.encoding,
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
