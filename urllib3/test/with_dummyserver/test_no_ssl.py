"""
Test connections without the builtin ssl module

Note: Import urllib3 inside the test functions to get the importblocker to work
"""
import pytest
from ..test_no_ssl import TestWithoutSSL

from dummyserver.testcase import HTTPDummyServerTestCase, HTTPSDummyServerTestCase
from dummyserver.server import (DEFAULT_CA)

import urllib3

# Retry failed tests
pytestmark = pytest.mark.flaky


class TestHTTPWithoutSSL(HTTPDummyServerTestCase, TestWithoutSSL):
    def test_simple(self):
        with urllib3.HTTPConnectionPool(self.host, self.port) as pool:
            r = pool.request("GET", "/")
            assert r.status == 200, r.data


class TestHTTPSWithoutSSL(HTTPSDummyServerTestCase, TestWithoutSSL):
    def test_simple(self):
        with urllib3.HTTPSConnectionPool(
            self.host, self.port, ca_certs=DEFAULT_CA, cert_reqs="NONE"
        ) as pool:
            try:
                pool.request("GET", "/")
            except urllib3.exceptions.SSLError as e:
                assert "SSL module is not available" in str(e)
