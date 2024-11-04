import json

try:
    import httplib
except ImportError:
    import http.client as httplib
import urllib.request
import urllib.parse


class HttpRequest:
    def __init__(self):
        self.host = ""
        self.path = ""
        self.params = {}
        self.headers = {}
        self.body = ""
        self.connectTimeout = 1000
        self.readTimeout = 10000
        self.useHttps = True


class HttpResponse:
    def __init__(self):
        self.statusCode = 0
        self.headerMap = {}
        self.body = ""
        return


class DefaultHttpClient:
    def __init__(self):
        return

    def post(self, http_request):
        if http_request.useHttps:
            connection = httplib.HTTPSConnection(http_request.host)
        else:
            connection = httplib.HTTPConnection(http_request.host)
        url = http_request.path + "?" + urllib.parse.urlencode(http_request.params)
        connection.request("POST", url, http_request.body.encode("utf-8"), http_request.headers)
        response = connection.getresponse()
        body = response.read()
        ret = HttpResponse()
        ret.body = body.decode("utf-8")
        ret.statusCode = response.status.real
        return ret
