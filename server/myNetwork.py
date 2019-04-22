import docker


class Network:
    client = docker.from_env()
    resourceID = base_url = 'unix://var/run/docker.sock'

    def list_all_networks(self):
        return (docker.APIClient(self.resourceID).networks())

#
# net = Network()
# net.list_all_networks()
