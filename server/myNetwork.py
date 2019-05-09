import docker


class Network:
    client = docker.from_env()
    resourceID = base_url = 'unix://var/run/docker.sock'

    def list_all_networks(self):
        return (docker.APIClient(self.resourceID).networks())

    def remove_network(self, network_id):
        return docker.APIClient(docker).remove_network(network_id)

    def get_network_by_id(self, net_id):
        return docker.APIClient(self.resourceID).inspect_network(net_id)

    def create_network(self, name, driver, *args):
        arg = None
        for i in args:
            arg = i
        output = self.client.networks.create(name, driver,
                                           ipam=arg)

        return output


#
#
net = Network()
# # net.list_all_networks()
# print(net.get_network_by_id('26c8963080a0f2e9921e6193482943e1e74c80f97fa5a3ef4ba1377c128eb0ea'))

# print(net.remove_network('26c8963080a0f2e9921e6193482943e1e74c80f97fa5a3ef4ba1377c128eb0ea'))
