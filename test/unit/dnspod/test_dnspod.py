# coding=utf-8
from dns.dnspod import *


def test_dnspod():

    login_token = ""
    domain_name = "wserver.cc"
    domain_id = ""

    print "DomainList"
    api = DomainList(login_token=login_token)
    print api().get("domains")

    print "get domain's domain_id"
    api = DomainList(login_token=login_token)
    domains = api().get("domains", {})
    for domain in domains:
        if domain.get("name") == domain_name:
            domain_id = domain.get("id")
        else:
            print "There isn't a domain named wserver.cc"

    print "RecordType"
    api = RecordType("D_Ultra", login_token=login_token)
    print api().get("types")

    print "RecordLine"
    api = RecordLine("D_Free", login_token=login_token)
    print api().get("lines")

    print "RecordCreate"
    api = RecordCreate("www", "A", u'默认'.encode("utf8"), '1.1.1.1', 600, domain_id=domain_id,
                       login_token=login_token)
    record = api().get("record", {})
    record_id = record.get("id")
    print "Record id", record_id

    print "RecordList"
    api = RecordList(domain_id, login_token=login_token)
    print api().get("records")

    print "DomainRemove"
    api = DomainRemove(domain_id, login_token=login_token)
    print api()

