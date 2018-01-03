import os
import time
from keystoneclient.auth.identity import v3
from keystoneclient import session
from keystoneclient.v3 import client as keystoneapi
from novaclient import client as novaapi

auth_url = 'http://192.168.10.220:5000/v3'
username = 'admin'
user_domain_admin = 'Default'
project_name = 'admin'
project_domain_name = 'Default'
password = 'admin'
auth = v3.Password(auth_url=auth_url,
                   username=username,
                   password=password,
                   project_name=project_name,
                   project_domain_name=project_domain_name,
                   )
sess = session.Session(auth=auth)
keystone = keystoneapi.Client(session=sess)
print keystone.projects.list()
#nova = novapi.Client(2, session=keystone.session)
#nova.images.list()  列出所有镜像
#image = nova.images.find(name='cirros-0.3.4-x86_64-uec')
#nova.flavors.list()  列出所有主机类型
#flavor = nova.flavors.find(name='m1.tiny')
#nova.networks.list()  列出所有网络
#network = nova.networks.find(label='ext')
#创建虚拟机
#server = nova.servers.create(name="vm_api", image=image, flavor=flavor,nics=[{'net-id':network.id}])
#print server

k={'Name': 'Zara', 'Age': 7, 'Class': 'First'}

k.viewkeys()
