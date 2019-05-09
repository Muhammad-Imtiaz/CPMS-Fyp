import docker


class Secrets:
    client = docker.from_env()
    resourceID = base_url = 'unix://var/run/docker.sock'

    def list_all_secrets(self):
        return self.client.secrets.list()


#
# net = Network()
# net.list_all_networks()

sec = Secrets()
print(sec.list_all_secrets())