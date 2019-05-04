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

    def create_network(self, name, driver, ipm):
        return self.client.networks.create(name=name, driver=driver, ipam=ipm)


#
# net = Network()
# # net.list_all_networks()
# print(net.get_network_by_id('1c358ae30e77a524e86f17f11e7b96407bc228fb9895cf843f6ed05b95ba6f88')['IPAM']['Config'][0])
