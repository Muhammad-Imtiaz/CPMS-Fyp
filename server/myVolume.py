import docker


# Manage volumes

class Volume:
    client = docker.from_env()
    resourceID = base_url = 'unix://var/run/docker.sock'

    def list_all_volumes(self):
        # print('List volumes')
        volumes = docker.APIClient(self.resourceID).volumes()
        return volumes['Volumes']
        # for i, v in enumerate(volumes):
        #     print(volumes['Volumes'][i]['Driver'])
        #     break
        # print(volumes)

    # Create a volume
    def create_volume(self, nameVol=None, driver=None, driver_opts=None, labels=None):
        print('creating volume ' + nameVol)
        docker.APIClient(self.resourceID).create_volume(nameVol, driver, driver_opts, labels)
        print('Volume created successfully....')

    # List volumes

    # print(self.client.volumes.list())

    # Display detailed information on one or more volumes
    def inspect_volume(self, nameVol):
        print('Display detailed information on one or more volumes')
        print(docker.APIClient(self.resourceID).inspect_volume(nameVol))

    # Remove one or more volumes
    def remove_volume(self, nameVol, force=False):
        print('Remove one or more volumes' + nameVol)
        docker.APIClient(self.resourceID).remove_volume(nameVol, force)

        print('Volume removed successfully ...')


#
vol = Volume()
vol.list_all_volumes()
# print(vol.list_volume())
# vol.inspect_volume('0629ac1be2402ed0b2347fcb6af9977cd46226f545f7871378154fce266eb600 ')
