import httplib
import urllib
import json


class Bitbucket:
    def __init__(self, user, password, **kw):
        self.base_url = "git.wserver.cc/rest/api/1.0"

        self.params = dict(
            user=user,
            password=password,
            format="json",
        )
        self.params.update(kw)
        self.path = None

    def request(self, **kw):
        self.params.update(kw)

        if not self.path:
            """Class pro will auto request path /pro."""
            name = self.__class__.__name__
            self.path = "/" + name
        conn = httplib.HTTPConnection(self.base_url)
        headers = {"Content-type": "application/json",
                   "User-Agent": "bitbucket-python/v1.0 (disable@126.com; Bitbucket Server API v1.0)"}
        conn.request("POST", self.path, urllib.urlencode(self.params), headers)

        response = conn.getresponse()
        data = response.read()
        conn.close()
        ret = json.loads(data)
        if ret.get("status", {}).get("code") == "1":
            return ret
        else:
            raise Exception(ret)

    __call__ = request


class project:
    def __init__(self):
        pass


class repo:
    def __init__(self):
        pass


class admin:
    def __init__(self):
        pass


class users:
    def __init__(self):
        pass


class logs:
    def __init__(self):
        pass


class hooks:
    def __init__(self):
        pass


