# encoding=utf-8
from docker.client import Client
import docker
import arrow
import re
import os
from docker.tls import TLSConfig
from docker.utils.utils import kwargs_from_env

IP = '115.29.146.79'
CERTS_DIR_PATH = '/home/zihua/Repository/violent_python/chapter10'

AUTH_CONFIG = (
    (
        os.path.join(CERTS_DIR_PATH, 'cert.pem'),
        os.path.join(CERTS_DIR_PATH, 'key.pem')
    ),
    os.path.join(CERTS_DIR_PATH, 'ca.pem')
)


def tls_config():
    from docker.tls import TLSConfig
    cert, _ = AUTH_CONFIG
    return TLSConfig(client_cert=cert, verify=False)


def docker_client(version='auto', base_url=None, tls=False, **kwargs):
    kwargs = kwargs_from_env(**kwargs)
    kwargs['version'] = version
    kwargs['base_url'] = base_url
    if tls:
        cert, _ = AUTH_CONFIG
        kwargs['tls'] = TLSConfig(client_cert=cert, verify=False)
    return Client(**kwargs)


def build():
    client = docker_client(base_url='tcp://%s:2376' % IP, tls=True)
    print client.info()
    client.containers.run("alpine", ["echo", "hello", "world"])


if __name__ == '__main__':
    build()
