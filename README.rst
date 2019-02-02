************
webtest-asgi
************

.. image:: https://badgen.net/pypi/v/webtest-asgi
  :alt: pypi badge
  :target: https://pypi.org/project/webtest-asgi/

.. image:: https://badgen.net/travis/sloria/webtest-asgi/master
  :alt: travis-ci status
  :target: https://travis-ci.org/sloria/webtest-asgi

.. image:: https://badgen.net/badge/code%20style/black/000
   :target: https://github.com/ambv/black
   :alt: Code style: Black

webtest-asgi provides integration of `WebTest <https://docs.pylonsproject.org/projects/webtest/>`_ with  `ASGI <https://asgi.readthedocs.io/>`_ applications.

Disclaimer
==========

You should probably use Starlette's `TestClient <https://www.starlette.io/testclient/>`_ 
instead of this package for testing ASGI applications. 
This package was created to test `webargs-starlette <https://github.com/sloria/webargs-starlette>`_ using
webargs' ``CommonTestCase``, which uses WebTest to test common
functionality across multiple web frameworks.

Installation
============
::

    pip install webtest-asgi


Usage
=====

You can use webtest-asgi with any ASGI application. Here is example usage with `Starlette <https://github.com/encode/starlette>`_.

.. code-block:: python

    from starlette.applications import Starlette
    from starlette.responses import JSONResponse
    from webtest_asgi import TestApp as WebTestApp

    app = Starlette()


    @app.route("/")
    async def homepage(request):
        return JSONResponse({"hello": "world"})


    @pytest.fixture()
    def testapp():
        return WebTestApp(app)


    def test_get_homepage(testapp):
        assert testapp.get("/").json == {"hello": "world"}


Project Links
=============

- PyPI: https://pypi.python.org/pypi/webtest-asgi
- Issues: https://github.com/sloria/webtest-asgi/issues

License
=======

MIT licensed. See the bundled `LICENSE <https://github.com/sloria/webtest-asgi/blob/master/LICENSE>`_ file for more details.
