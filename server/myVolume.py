import docker

# Manage volumes

class Volume:

    client = docker.from_env()
    resourceID = base_url = 'unix://var/run/docker.sock'

    # Create a volume
    def create_volume(self, nameVol=None, driver=None, driver_opts=None, labels=None):
        print('creating volume ' + nameVol)
        docker.APIClient(self.resourceID).create_volume(nameVol, driver, driver_opts, labels)
        print('Volume created successfully....')

    # List volumes
    def list_volume(self):
        print('List volumes')
        print(self.client.volumes.list())

    # Display detailed information on one or more volumes
    def inspect_volume(self, nameVol):
        print('Display detailed information on one or more volumes')
        print(docker.APIClient(self.resourceID).inspect_volume(nameVol))

    # Remove one or more volumes
    def remove_volume(self, nameVol, force=False):
        print('Remove one or more volumes' + nameVol)
        docker.APIClient(self.resourceID).remove_volume(nameVol, force)
        print('Volume removed successfully ...')
