import re
from setuptools import setup

INSTALL_REQUIRES = [
    "webtest",
    "starlette>=0.9.0",
    # Needed by starlette's TestClient
    "requests",
    # Needed by starlette for form parsing
    "python-multipart",
]

EXTRAS_REQUIRE = {
    "tests": ["pytest"],
    "lint": ["flake8==3.6.0", "flake8-bugbear==18.8.0", "pre-commit==1.13.0"],
}
EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["lint"] + ["tox"]


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ""
    with open(fname, "r") as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError("Cannot find version information")
    return version


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name="webtest-asgi",
    version=find_version("webtest_asgi.py"),
    description="webtest-asgi provides integration of WebTest with ASGI applications",
    long_description=read("README.rst"),
    author="Steven Loria",
    author_email="sloria1@gmail.com",
    url="https://github.com/sloria/webtest-asgi",
    py_modules=["webtest_asgi"],
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    license="MIT",
    zip_safe=False,
    keywords="webtest-asgi webtest testing asgi wsgi asyncio",
    classifiers=[
        "Intended Audience :: Developers",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Testing",
    ],
)
