from math import ceil

import docker


class System:
    client = docker.from_env()
    resourceID = base_url = 'unix://var/run/docker.sock'

    # Display system-wide information
    def docker_system_info(self):
        print('Display system-wide information')
        info = docker.APIClient(self.resourceID).info()
        print(info)
        ncpu = info['NCPU']
        name = info['Name']
        id = info['ID']
        osType = info['OSType']
        kernelVersion = info['KernelVersion']
        memory = ceil(info['MemTotal'] / 1024000000)
        serverVersion = info['ServerVersion']
        driver = info['Driver']
        httpProxy = info['HttpProxy']
        registery = info['IndexServerAddress']

        network = info['Plugins']['Network']
        print(network)

        vol_plugin = info['Plugins']['Volume'][0]
        # print(vol)

        # preparing output
        output = {'NCPU': ncpu, 'Name': name, 'ID': id, 'OSType': osType, 'KernelVersion': kernelVersion,
                  'Memory': memory,
                  'ServerVersion': serverVersion, 'Driver': driver, 'HttpProxy': httpProxy,
                  'IndexServerAddress': registery, 'Network':network, 'VolumePlugins':vol_plugin}
        return output

    # Show docker disk usage
    def docker_system_disk_usage(self):
        print('Show docker disk usage')
        print(docker.client.APIClient(self.resourceID).df())

    # Get real time events from the server
    def docker_system_events(self, since=None, until=None, filters=None, decode=None):
        print('Get real time events from the server')
        print(docker.APIClient(self.resourceID).events(since, until, filters, decode))


sys = System()
# sys.docker_system_info()
# sys.docker_system_disk_usage()
# print('Test' == 'Test')
