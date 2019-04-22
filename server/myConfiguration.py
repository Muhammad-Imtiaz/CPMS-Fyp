import docker


class Configuration:
    client = docker.from_env()
    resourceID = base_url = 'unix://var/run/docker.sock'

    def list_all_configurations(self):
        return (docker.APIClient(self.resourceID).services())

#
# net = Network()
# net.list_all_networks()
