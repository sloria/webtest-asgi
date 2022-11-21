import re
from setuptools import setup

INSTALL_REQUIRES = [
    "webtest",
    "starlette>=0.21.0",
    "httpx~=0.23.0",  # starlette >= v0.21.0 requires httpx for TestClient
    # Needed by starlette for form parsing
    "python-multipart",
]

EXTRAS_REQUIRE = {
    "tests": ["pytest"],
    "lint": ["flake8==5.0.4", "flake8-bugbear==22.10.27", "pre-commit~=2.20"],
}
EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["lint"] + ["tox"]


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ""
    with open(fname) as fp:
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
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Testing",
    ],
)
