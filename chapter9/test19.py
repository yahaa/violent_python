# encoding=utf-8
from inspect import getdoc
from colorama.ansi import Fore, Style
import os


DOCKER_SOCKET_PATH = "/var/run/docker.sock"
SETTING_DIR_PATH = "/etc/daocloud/dce"
DATA_DIR_PATH = "/var/local/dce"


class Test(object):
    """
    测试
    """

    def dcc(self):
        print getdoc(self)


t = Test()
t.dcc()


print Fore.CYAN + Style.BRIGHT + " AKSLDJFASDF"


run_manager_command = ('docker run --rm -it '
                       '-v {host_socket_path}:{socket_path} '
                       '-v {host_setting_dir}:{setting_dir} '
                       '-v {host_data_dir}:{data_dir} '
                       '{extra_arguments} '
                       '{bootstrap_repo_name} ').format(
    host_socket_path=DOCKER_SOCKET_PATH,
    socket_path=DOCKER_SOCKET_PATH,
    host_setting_dir=SETTING_DIR_PATH,
    setting_dir=os.path.dirname(SETTING_DIR_PATH),
    host_data_dir=DATA_DIR_PATH,
    data_dir=os.path.dirname(DATA_DIR_PATH),
    extra_arguments="",
    bootstrap_repo_name="daocloud.io/daocloud/dce"
)

print run_manager_command

run_manager_command = "%s do-%s %s" % (run_manager_command,
                                       "install", "")

print run_manager_command


class Rest():
    def t1(self):
        print "test 1"

    def perform(self, *args):
        print args
        raise NotImplementedError()

    def parse(self):
        return getattr(self, "t1"), 1, 2

    def ttto(self):
        self.perform(*self.parse())


rest = Rest()
rest.ttto()
