import docker


class Service:
    client = docker.from_env()
    resourceID = base_url = 'unix://var/run/docker.sock'

    def list_all_services(self):
        return self.client.services.list()

#
# net = Network()
# net.list_all_networks()
serv = Service()
print(serv.list_all_services())