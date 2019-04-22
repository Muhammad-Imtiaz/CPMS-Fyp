import docker


class Service:
    client = docker.from_env()
    resourceID = base_url = 'unix://var/run/docker.sock'

    def list_all_services(self):
        return (docker.APIClient(self.resourceID).services())

#
# net = Network()
# net.list_all_networks()
