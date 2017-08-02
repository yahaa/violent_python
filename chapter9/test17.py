
from docker.client import Client
import docker
import arrow
import re
import os
from docker.tls import TLSConfig
from docker.utils.utils import kwargs_from_env

CLIENT_CERTS_DIR_PATH = '/home/zihua/Repository/violent_python/chapter9'

CLIENT_CERT_AUTH_CONFIG = (
    (
        os.path.join(CLIENT_CERTS_DIR_PATH, 'client-cert.pem'),
        os.path.join(CLIENT_CERTS_DIR_PATH, 'client-key.pem')
    ),
    os.path.join(CLIENT_CERTS_DIR_PATH, 'ca.pem')
)


def t():
    """
        Run DCE Base Server.

        Usage: base [options]

        Description:
          The command will run DCE base.

        Options:
          --mode MODE                      Initialize the mode of the cluster.  [MODE]
          --force-pull                     Always Pull Image, default is pull when missing. [FORCE_PULL]
          --swarm-port PORT                Specify the swarm manager port(default: 2376). [SWARM_PORT]
          --controller-port PORT           Specify the dce controller port(default: 80). [CONTROLLER_PORT]
          --controller-ssl-port PORT       Specify the dce controller ssl port(default: 443). [CONTROLLER_SSL_PORT]
          --pod-cluster-cidr CIDR          CIDR Range for Pods in cluster (default 172.28.0.0/16). [POD_CLUSTER_CIDR]
          --service-cluster-ip-range CIDR  A CIDR notation IP range from which to assign service cluster IPs (default 10.96.0.0/12). [SERVICE_CLUSTER_IP_RANGE]
          --service-node-port-range RANGE  A port range to reserve for services with NodePort visibility (default 30000-32767). [SERVICE_NODE_PORT_RANGE]
          --kube-dns-cluster-ip IP         Specify the kube dns service cluster ip. [KUBE_DNS_CLUSTER_IP]
          --disable-resource-limit         Disable resource limit for system containers. [NO_RESOURCE_LIMIT]
          --network-driver                 Select network driver (calico | flannel | none) (default calico)
        """
    print '123456'


def tls_config():
    from docker.tls import TLSConfig
    cert, _ = CLIENT_CERT_AUTH_CONFIG
    return TLSConfig(client_cert=cert, verify=False)


def docker_client(version='auto', base_url=None, tls=False, **kwargs):
    kwargs = kwargs_from_env(**kwargs)
    kwargs['version'] = version
    kwargs['base_url'] = base_url
    if tls:
        cert, _ = CLIENT_CERT_AUTH_CONFIG
        kwargs['tls'] = TLSConfig(client_cert=cert, verify=False)
    return Client(**kwargs)


# def docker_client(**kwargs):
#     cert, _ = CLIENT_CERT_AUTH_CONFIG
#     kwargs['version'] = 'auto'
#     kwargs['tls'] = TLSConfig(client_cert=cert, verify=False)
#     return Client(**kwargs)


# client = docker_client(environment={}, ssl_version='auto',
#                        assert_hostname='tcp://%s:12376' % '192.168.100.182')


def convert_docker_datetime(datetime_str):
    def is_num(c): return re.match(r'\d', c) is not None
    p_pos = datetime_str.rfind('.')
    if p_pos < 0:
        return datetime_str
    tz_pos = None
    for i, c in enumerate(datetime_str[p_pos + 1:]):
        if not is_num(c):
            tz_pos = i + p_pos
            break

    micro_sec = datetime_str[p_pos:tz_pos][1:6]
    validated_datetime_str = datetime_str[:p_pos] + '.' + micro_sec
    if tz_pos:
        validated_datetime_str += datetime_str[tz_pos:]
    return validated_datetime_str


def get_controller_time():
    # environment = {'DOCKER_HOST': 'http://%s:2377' % '192.168.100.182'}
    # print environment
    # cert, _ = CLIENT_CERT_AUTH_CONFIG
    # kwargs = kwargs_from_env(assert_hostname=False)
    # # kwargs['version'] = 'auto'
    #
    # kwargs['tls'] = TLSConfig(client_cert=cert, verify=False)
    # kwargs['base_url'] = 'tcp://%s:12376' % '192.168.100.182'
    c = docker_client(base_url='tcp://%s:12376' %
                      '192.168.100.182', tls=True)
    # c = docker_client(environment={})

    # c = docker_client(**kwargs)
    # print c.info()
    return c.info().get('SystemTime')


def get_time_drift_from_controller():
    print get_controller_time()
    t1 = arrow.now()
    t2 = arrow.get(convert_docker_datetime(get_controller_time()))
    t3 = arrow.now()
    t4 = arrow.get(convert_docker_datetime(get_controller_time()))
    t5 = arrow.now()
    print t1
    print t2
    print t3
    print t4
    print t5

    drift = abs(
        ((t1 - t2).total_seconds() + 2 * (t3 - t4).total_seconds() + (t5 - t2).total_seconds()) / 4) * 10 ** 3

    # drift = abs(((t1 / 2 - t2 + t3 - t4 + t5 / 2) / 2) * 10 ** 3)
    return drift


print 'time offset is %.3f' % get_time_drift_from_controller()
