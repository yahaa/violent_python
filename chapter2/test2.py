import pexpect
child = pexpect.spawn('python')
print child.expect(['>>>'])
print child.before
