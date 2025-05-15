*********
Changelog
*********

2.0.0 (2025-05-14)
==================

Fixes:

* Remove upper bound on httpx version.

Other:

* Test against Python 3.9-3.13.
* Support starlette>=0.38.0.
* Support httpx>=0.27.1.
* **Backwards-incompatible**: Drop support for Python 3.8.
* **Backwards-incompatible**: Remove `webtest_asgi.__version__`.
  Use `importlib.metadata("webtest-asgi")` instead.

1.1.0 (2022-11-21)
==================

Features:

* **Backwards-incompatible**: Support starlette>=0.21.0. 
  Drop support for older starlette versions.
  Thanks @DmitryBurnaev for the PR.

Other:

* Test against Python 3.8-3.11.
* **Backwards-incompatible**: Drop support for Python 3.6.

1.0.1 (2019-01-03)
==================

Bug fixes:

* Fix passing of duplicate query parameters.

1.0.0 (2019-01-02)
==================

* First release.
