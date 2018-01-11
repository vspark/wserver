# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 采用26个英文字母(区分大小写)和0-9的自然数(经常不需要)加上下划线'_'组成，命名简洁明确，多个单词用下划线'_'分隔
# 全部小写命名
# 字段必须填写描述信息
# 禁止使用数据库关键字，如：name，time ，datetime password 等
# 示例：user_id user_name sex
from django.utils import timezone


class idc(models.Model):
    idc_name = models.CharField(max_length=128, null=False)
    idc_type = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=128, null=False)
    service_time = models.DateField(blank=False)
    contact = models.CharField(max_length=30, null=False)
    stack = models.CharField(max_length=128, null=True)
    bandwidth = models.CharField(max_length=10, null=True)
    create_time = models.DateTimeField(default=timezone.now, editable=True)
    update_time = models.DateTimeField(default=timezone.now, editable=True)


class stack(models.Model):
    stack_name = models.CharField(max_length=128, null=False)
    position = models.CharField(max_length=128, null=False)
    height = models.CharField(max_length=20, null=False)
    supply_voltage = models.CharField(max_length=20, null=False)
    limit_current = models.CharField(max_length=20, null=False)
    pdu_type = models.CharField(max_length=20, null=False)
    create_time = models.DateTimeField(default=timezone.now, editable=True)
    update_time = models.DateTimeField(default=timezone.now, editable=True)


class wan(models.Model):
    wan_name = models.CharField(max_length=128, null=False)
    wan_type = models.CharField(max_length=20, null=False)
    provider = models.CharField(max_length=128, null=False)
    port_type = models.CharField(max_length=20, null=False)
    to = models.CharField(max_length=128, null=False)
    to_ip = models.GenericIPAddressField()
    our_ip = models.GenericIPAddressField()
    business = models.CharField(max_length=128, null=False)
    data_direction = models.CharField(max_length=20, null=False)
    stack_id = models.CharField(max_length=10, null=False)
    device_id = models.CharField(max_length=10, null=False)
    device_port = models.CharField(max_length=10, null=False)
    create_time = models.DateTimeField(default=timezone.now, editable=True)
    update_time = models.DateTimeField(default=timezone.now, editable=True)


class device(models.Model):
    device_name = models.CharField(max_length=128, null=False)
    vendor = models.CharField(max_length=128, null=False)
    device_type = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    parameters = models.CharField(max_length=128, null=False)
    stack_id = models.CharField(max_length=10, null=False)
    position = models.CharField(max_length=20, null=False)
    host_device_id = models.CharField(max_length=10, null=False)
    height = models.CharField(max_length=20, null=False)
    uplink_device = models.CharField(max_length=10, null=False)
    uplink_port = models.CharField(max_length=10, null=False)
    service_time = models.DateField(blank=False)
    ip = models.GenericIPAddressField()
    mac = models.CharField(max_length=16, null=False)
    serial_no = models.CharField(max_length=128, null=False)
    create_time = models.DateTimeField(default=timezone.now, editable=True)
    update_time = models.DateTimeField(default=timezone.now, editable=True)


class domain(models.Model):
    dm_name = models.CharField(max_length=128, null=False)
    dm_service = models.CharField(max_length=128, null=False)
    dm_service_time = models.DateField(blank=False)
    dm_environment = models.CharField(max_length=128, null=True)
    dm_project = models.CharField(max_length=128, null=True)
    dm_icp = models.CharField(max_length=128, null=True)
    create_time = models.DateTimeField(default=timezone.now, editable=True)
    update_time = models.DateTimeField(default=timezone.now, editable=True)


class dns(models.Model):
    rc_rr = models.CharField(max_length=128, null=False)
    rc_value = models.GenericIPAddressField(null=False)
    rc_type = models.CharField(max_length=128, null=False)
    rc_line = models.CharField(max_length=128, null=True)
    rc_priority = models.CharField(max_length=128, null=True)
    rc_ttl = models.CharField(max_length=128, null=False)
    rc_environment = models.CharField(max_length=128, null=True)
    rc_service = models.CharField(max_length=128, null=True)
    create_time = models.DateTimeField(default=timezone.now, editable=True)
    update_time = models.DateTimeField(default=timezone.now, editable=True)


class foo(models.Model):
    foo_name = models.CharField(max_length=20, null=False)
    foo_bar = models.CharField(max_length=128, null=False)



