from datetime import datetime
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import json

from cmdb import models
from cmdb.models import device


def foo(request):
    return render(request, 'cmdb/foo.html')


def view(request):
    return render(request, 'cmdb/view.html')


def installations(request):
    return render(request, 'cmdb/view.html')


def statistics(request):
    return render(request, 'cmdb/view.html')


def ip(request):
    return render(request, 'cmdb/view.html')


def keys(request):
    return render(request, 'cmdb/view.html')


def basesoft(request):
    return render(request, 'cmdb/view.html')


def vms(request):
    return render(request, 'cmdb/view.html')


def net(request):
    return render(request, 'cmdb/view.html')


@login_required(login_url="/login/")
def device_view(request):
    filter = request.GET.get('filter', "")
    if filter:
        p_device = device.objects.filter(Q(device_name__contains=filter) |
                                         Q(device_type__contains=filter) |
                                         Q(model__contains=filter) |
                                         Q(serial_no__contains=filter) |
                                         Q(ip__exact=filter))
    else:
        p_device = device.objects.all()

    NUM_PER_PAGE = 10
    paginater = Paginator(p_device, NUM_PER_PAGE)
    page = request.GET.get('page')

    try:
        contexts = paginater.page(page)
    except PageNotAnInteger:
        contexts = paginater.page(1)
    except EmptyPage:
        contexts = paginater.page_range(paginater.num_pages)

    return render_to_response('cmdb/device.html', {'device': contexts, 'filter': filter})
    pass

@login_required(login_url="/login/")
def idc_query(request):
    try:
        post = json.loads(request.body)
        print post
        db_idc = models.device.objects.get(pk=post["pk"])
        p = {
            '_name': db_idc.idc_name,
            'idc_type': db_idc.idc_type,
            'address': db_idc.address,
            'service_time': str(db_idc.service_time),
            'contact': db_idc.contact,
            'stack': db_idc.stack,
            'bandwidth': db_idc.bandwidth
        }
        context = {"flag": "Success", "context": {"db_idc": p}}
    except Exception, e:
        context = {"flag": "Error", "context": str(e)}
    return HttpResponse(json.dumps(context))
    pass


@login_required(login_url="/login/")
def idc_view(request):
    filter = request.GET.get('filter', "")
    if filter:
        p_idc = models.idc.objects.filter(Q(idc_name__contains=filter) |
                                          Q(address__contains=filter) |
                                          Q(idc_type__contains=filter))
    else:
        p_idc = models.idc.objects.all()

    NUM_PER_PAGE = 10
    paginater = Paginator(p_idc, NUM_PER_PAGE)
    page = request.GET.get('page')

    try:
        contexts = paginater.page(page)
    except PageNotAnInteger:
        contexts = paginater.page(1)
    except EmptyPage:
        contexts = paginater.page_range(paginater.num_pages)

    return render_to_response('cmdb/idc.html', {'idc': contexts, 'filter': filter})
    pass


@login_required(login_url="/login/")
def idc_query(request):
    try:
        post = json.loads(request.body)
        print post
        db_idc = models.idc.objects.get(pk=post["pk"])
        p = {
            'idc_name': db_idc.idc_name,
            'idc_type': db_idc.idc_type,
            'address': db_idc.address,
            'service_time': str(db_idc.service_time),
            'contact': db_idc.contact,
            'stack': db_idc.stack,
            'bandwidth': db_idc.bandwidth
        }
        context = {"flag": "Success", "context": {"db_idc": p}}
    except Exception, e:
        context = {"flag": "Error", "context": str(e)}
    return HttpResponse(json.dumps(context))
    pass


@login_required(login_url="/login/")
def idc_save(request):
    try:
        post = json.loads(request.body)
        idc_id              = post['base_config']['idc_id']
        idc_name            = post['base_config']['idc_name']
        idc_type            = post['base_config']['idc_type']
        idc_address         = post['base_config']['idc_address']
        idc_service_time    = post['base_config']['idc_service_time']
        idc_contact         = post['base_config']['idc_contact']
        idc_stack           = post['base_config']['idc_racks']
        idc_bandwidth       = post['base_config']['idc_bandwidth']

        db_idc = {
            'idc_name': idc_name,
            'idc_type': idc_type,
            'address': idc_address,
            'service_time': idc_service_time,
            'contact': idc_contact,
            'stack': idc_stack,
            'bandwidth': idc_bandwidth,
            'update_time': datetime.now()
        }

        if not idc_id:
            models.idc.objects.create(**db_idc)
        else:
            models.idc.objects.filter(id=idc_id).update(**db_idc)
            models.idc.objects.get(id=idc_id)
        context = {"flag": "Success"}

    except Exception, e:
        context = {"flag": "Error", "context": str(e)}

    return HttpResponse(json.dumps(context))
    pass


@login_required(login_url="/login/")
def idc_delete(request):
    try:
        post = json.loads(request.body)
        idc_db = models.idc.objects.get(pk=post['pk'])
        idc_db.delete()
        context = {"flag": "Success"}
    except Exception, e:
        context = {"flag": "Error", "context": str(e)}
    return HttpResponse(json.dumps(context))
    pass


@login_required(login_url="/login/")
def foo_save(request):
    try:
        post = json.loads(request.body)
        name = post['foo_base_config']['foo_foo_name']
        bar = post['foo_base_config']['foo_foo_bar']

        db_foo = {
            'foo_name': name,
            'foo_bar': bar,
        }

        models.foo.objects.create(**db_foo)
        context = {"flag": "Success"}

    except Exception, e:
        context = {"flag": "Error", "context": str(e)}

    return HttpResponse(json.dumps(context))
    pass