import pytest
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from webtest_asgi import TestApp as WebTestApp


@pytest.fixture()
def app():
    app_ = Starlette()

    @app_.route("/")
    async def homepage(request):
        return JSONResponse({"hello": "world"})

    @app_.route("/echo_post", ["POST"])
    async def echo_post(request):
        form_body = await request.form()
        return JSONResponse(dict(form_body))

    @app_.route("/echo_json", ["POST"])
    async def echo_json(request):
        json_body = await request.json()
        return JSONResponse(json_body)

    @app_.route("/echo_headers", ["GET"])
    async def echo_headers(request):
        return JSONResponse(dict(request.headers))

    @app_.route("/echo_params", ["GET"])
    async def echo_params(request):
        return JSONResponse(dict(request.query_params))

    @app_.route("/always_error", ["GET"])
    async def always_error(request):
        return JSONResponse({"error": "oh no!"}, status_code=422)

    @app_.route("/multi", ["GET"])
    async def multi_param(request):
        return JSONResponse(request.query_params.getlist("name"))

    return app_


@pytest.fixture()
def wt(app):
    return WebTestApp(app)


def test_get(wt):
    res = wt.get("/")
    assert res.status_code == 200
    expected = {"hello": "world"}
    assert res.json == expected


def test_post_form(wt):
    res = wt.post("/echo_post", {"name": "Steve"})
    assert res.json == {"name": "Steve"}


def test_post_json(wt):
    res = wt.post_json("/echo_json", {"name": "Steve"})
    assert res.json == {"name": "Steve"}


def test_headers(wt):
    res = wt.get("/echo_headers", headers={"X-Foo": "Bar"})
    assert res.json["x-foo"] == "Bar"


def test_params(wt):
    res = wt.get("/echo_params?foo=bar")
    assert res.json == {"foo": "bar"}


def test_error(wt):
    res = wt.get("/always_error", expect_errors=True)
    assert res.json == {"error": "oh no!"}
    assert res.status_code == 422


def test_404(wt):
    res = wt.get("/not_found", expect_errors=True)
    assert res.status_code == 404


def test_multi_param(wt):
    res = wt.get("/multi?name=Steve&name=Loria")
    assert res.json == ["Steve", "Loria"]
