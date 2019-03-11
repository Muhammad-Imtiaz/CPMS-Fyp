import docker

#manage docker system

class System:

    client = docker.from_env()
    resourceID = base_url = 'unix://var/run/docker.sock'

    #Display system-wide information
    def docker_system_info(self):
        print('Display system-wide information')
        print(docker.APIClient(self.resourceID).info())


    # Show docker disk usage
    def docker_system_disk_usage(self):
        print('Show docker disk usage')
        print(docker.client.APIClient(self.resourceID).df())

    # Get real time events from the server
    def docker_system_events(self, since=None, until=None, filters=None, decode=None):
        print('Get real time events from the server')
        print(docker.APIClient(self.resourceID).events(since, until, filters, decode))
