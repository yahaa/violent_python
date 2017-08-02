import docker
client = docker.from_env()
print client.containers().list()
