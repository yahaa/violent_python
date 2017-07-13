import time
import re
import docker
import arrow
import datetime

c = docker.from_env()


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


info = c.info()
t = info.get('SystemTime')
tt = convert_docker_datetime(info.get('SystemTime'))
print arrow.now()
print convert_docker_datetime(info.get('SystemTime'))
# print time.time('2013-05-11T21:23:58.970460+00:00')
