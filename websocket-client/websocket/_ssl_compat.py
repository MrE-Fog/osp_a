"""
websocket - WebSocket client library for Python

Copyright (C) 2010 Hiroki Ohtani(liris)

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor,
    Boston, MA 02110-1335  USA

"""
__all__ = ["HAVE_SSL", "ssl", "SSLError", "get_ssl", "inject_wolfssl", "extract_wolfssl"]

SSL_MODULE=None

try:
    import ssl

    from ssl import SSLError
    if hasattr(ssl, 'SSLContext') and hasattr(ssl.SSLContext, 'check_hostname'):
        HAVE_CONTEXT_CHECK_HOSTNAME = True
    else:
        HAVE_CONTEXT_CHECK_HOSTNAME = False
        if hasattr(ssl, "match_hostname"):
            from ssl import match_hostname
        else:
            from backports.ssl_match_hostname import match_hostname
        __all__.append("match_hostname")
    __all__.append("HAVE_CONTEXT_CHECK_HOSTNAME")

    HAVE_SSL = True
    SSL_MODULE = ssl

except ImportError:
    # dummy class of SSLError for ssl none-support environment.
    class SSLError(Exception):
        pass

    HAVE_SSL = False

def get_ssl():
    return SSL_MODULE

def inject_wolfssl():
    import wolfssl
    global SSL_MODULE
    SSL_MODULE = wolfssl

def extract_wolfssl():
    global SSL_MODULE
    SSL_MODULE = ssl
