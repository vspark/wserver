import httplib
import urllib
import json
import re


class Dnspod:
    def __init__(self, login_token, **kw):
        self.base_url = "dnsapi.cn"

        self.params = dict(
            login_token=login_token,
            format="json",
        )
        self.params.update(kw)
        self.path = None

    def request(self, **kw):
        self.params.update(kw)
        if not self.path:
            """Class UserInfo will auto request path /User.Info."""
            name = re.sub(r'([A-Z])', r'.\1', self.__class__.__name__)
            self.path = "/" + name[1:]
        conn = httplib.HTTPSConnection(self.base_url)
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json",
                   "User-Agent": "dnspod-python/0.01 (disable@126.com; DNSPod.CN API v2.8)"}
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


class InfoVersion(Dnspod):
    pass


class UserDetail(Dnspod):
    pass


class UserInfo(Dnspod):
    pass


class UserLog(Dnspod):
    pass


class DomainCreate(Dnspod):
    def __init__(self, domain, **kw):
        kw.update(dict(domain=domain))
        Dnspod.__init__(self, **kw)


class DomainId(Dnspod):
    def __init__(self, domain, **kw):
        kw.update(dict(domain=domain))
        Dnspod.__init__(self, **kw)


class DomainList(Dnspod):
    pass


class _DomainApiBase(Dnspod):
    def __init__(self, domain_id, **kw):
        kw.update(dict(domain_id=domain_id))
        Dnspod.__init__(self, **kw)


class DomainRemove(_DomainApiBase):
    pass


class DomainStatus(_DomainApiBase):
    def __init__(self, status, **kw):
        kw.update(dict(status=status))
        _DomainApiBase.__init__(self, **kw)


class DomainInfo(_DomainApiBase):
    pass


class DomainLog(_DomainApiBase):
    pass


class RecordType(Dnspod):
    def __init__(self, domain_grade, **kw):
        kw.update(dict(domain_grade=domain_grade))
        Dnspod.__init__(self, **kw)


class RecordLine(Dnspod):
    def __init__(self, domain_grade, **kw):
        kw.update(dict(domain_grade=domain_grade))
        Dnspod.__init__(self, **kw)


class RecordCreate(_DomainApiBase):
    def __init__(self, sub_domain, record_type, record_line, value, ttl, mx=None, **kw):
        kw.update(dict(
            sub_domain=sub_domain,
            record_type=record_type,
            record_line=record_line,
            value=value,
            ttl=ttl,
        ))
        if mx:
            kw.update(dict(mx=mx))
        _DomainApiBase.__init__(self, **kw)


class RecordModify(RecordCreate):
    def __init__(self, record_id, **kw):
        kw.update(dict(record_id=record_id))
        RecordCreate.__init__(self, **kw)


class RecordList(_DomainApiBase):
    pass


class _RecordBase(_DomainApiBase):
    def __init__(self, record_id, **kw):
        kw.update(dict(record_id=record_id))
        _DomainApiBase.__init__(self, **kw)


class RecordRemove(_RecordBase):
    pass


class RecordDdns(_DomainApiBase):
    def __init__(self, record_id, sub_domain, record_line, **kw):
        kw.update(dict(
            record_id=record_id,
            sub_domain=sub_domain,
            record_type=record_type,
            record_line=record_line,
        ))
        _DomainApiBase.__init__(self, **kw)


class RecordStatus(_RecordBase):
    def __init__(self, status, **kw):
        kw.update(dict(status=status))
        _RecordBase.__init__(self, **kw)


class RecordInfo(_RecordBase):
    pass

