import os
CMD = '[Service]\n\
Restart={}\n\
RestartSec=3'

SYSTEMD_DOCKER_CONF_PATH = '/home/zihua/10-dce.conf'
SYSTEMD_RESTART_POLICYS = ['no', 'always', 'on-success',
                           'on-failure', 'on-abnormal', 'on-abort', 'on-watchdog']


def docker_restart_conf(policy=None):
    # if not policy:
    #     policy = 'on-failure'
    policy = policy if policy in SYSTEMD_RESTART_POLICYS else 'on-failure'
    config = '[Service]\n\
    Restart={}\n\
    RestartSec=3'.format(policy)
    filename = open(SYSTEMD_DOCKER_CONF_PATH, 'w')
    filename.write(config)
    filename.close()


docker_restart_conf('A')
