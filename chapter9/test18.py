import sys
import platform


def main():
    str = sys.argv[0:]
    print str


if __name__ == '__main__':
    check_subnet_command = """
SUBNET_172_STATE=`ip route | grep -E "^172\.1[6-9]" | grep -v -E "(docker|br-)" | wc -l | awk '{if($1 != 0){print "confliction"}else{print "no_confliction"}}'`
[[ $SUBNET_172_STATE = confliction ]]||SUBNET_172_STATE=`grep -v "^#" /etc/resolv.conf | grep -E "nameserver\s+172\.1[6-9]" | wc -l | awk '{if($1 != 0){print "confliction"}else{print "no_confliction"}}'`
SUBNET_10_STATE=`ip route | grep -E "^10\.255" | grep -v -E "(docker|br-)" | wc -l | awk '{if($1 != 0){print "confliction"}else{print "no_confliction"}}'`
[[ $SUBNET_10_STATE = confliction ]]||SUBNET_10_STATE=`grep -v "^#" /etc/resolv.conf | grep -E "nameserver\s+10\.255" | wc -l | awk '{if($1 != 0){print "confliction"}else{print "no_confliction"}}'`
"""
    print check_subnet_command
    print platform.uname()
    uname = " ".join(platform.uname())
    print uname
