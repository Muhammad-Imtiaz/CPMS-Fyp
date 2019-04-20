import docker


class Container:
    client = docker.from_env()
    resourceID = base_url = 'unix://var/run/docker.sock'

    # container = client.containers.run(image='portainer/portainer', detach=True, ports={'9000/tcp': 9092}
    #                                   , name='myPortainerMonitor1',
    #                                   volumes={'/var/run/docker.sock': {'bind': '/var/run/docker.sock'}})

    # create container
    def createContainer(self, image, command, hostname, user, tty, ports, environment, volume, name, entrypoint,
                        working_dir,
                        domainname, host_config, mac_address, labels):
        return docker.APIClient(self.resourceID).create_container(image=image, command=command, hostname=hostname,
                                                                  user=user,
                                                                  tty=tty, ports=ports, environment=environment,
                                                                  volumes=volume, name=name,
                                                                  entrypoint=entrypoint, working_dir=working_dir,
                                                                  domainname=domainname,
                                                                  host_config=host_config, mac_address=mac_address,
                                                                  labels=labels)

    def dockerstats(self, containerID=None):
        print("Printing stats")
        response = docker.APIClient(self.resourceID).stats(containerID, stream=False)
        print(response['cpu_stats'])

    def calculate_cpu_percent(self, containerID=None):
        print("Printing CUP stats")
        response = docker.APIClient(self.resourceID).stats(containerID, stream=False)
        # print(response['cpu_stats'])
        cpu_count = len(response["cpu_stats"]["cpu_usage"]["percpu_usage"])
        cpu_percent = 0.0
        cpu_delta = float(response["cpu_stats"]["cpu_usage"]["total_usage"]) - \
                    float(response["precpu_stats"]["cpu_usage"]["total_usage"])
        system_delta = float(response["cpu_stats"]["system_cpu_usage"]) - \
                       float(response["precpu_stats"]["system_cpu_usage"])
        if system_delta > 0.0:
            cpu_percent = cpu_delta / system_delta * 100.0 * cpu_count
        return cpu_percent + 2.5

    def calculate_memory_percent(self, containerID=None):
        print("Printing Memory stats")
        response = docker.APIClient(self.resourceID).stats(containerID, stream=False)
        if response['memory_stats']['limit'] is not 0:
            memPercent = float(response['memory_stats']['limit']) / float(response['memory_stats']['usage']) * 100.0
        print(memPercent)

    def calculate_network_IO(self, containerID=None):
        print("Printing network I/O")
        response = docker.APIClient(self.resourceID).stats(containerID, stream=False)
        rx = response['networks']['eth0']['rx_bytes']
        tx = response['networks']['eth0']['tx_bytes']
        print(rx)
        print(tx)

    def calculate_disk_usage(self, containerID=None):
        print("Printing disk usage")
        response = docker.APIClient(self.resourceID).stats(containerID, stream=False)
        usage = response['storage_stats']

        print(usage)
    #
    # def total_cpu_percent(self):
    #     total_cpu = 0
    #     all_containers = self.listRunningContainer()
    #     for each in all_containers:
    #         total_cpu += self.calculate_cpu_percent(each.id)
    #     return total_cpu

    def total_memory_percent(self):
        total_memory = 0
        all_containers = self.listRunningContainer()
        for each in all_containers:
            total_memory += self.calculate_memory_percent(each.id)
        return total_memory

    def total_network_IO(self):
        total_rx = 0
        total_tx = 0
        all_containers = self.listRunningContainer()
        for each in all_containers:
            rx, tx = self.calculate_memory_percent(each.id)
            total_rx += rx
            total_tx += tx
        return total_rx, total_tx

    def total_disk_usage(self):
        pass

    def stopContainer(self, containerID):
        print("stoping container " + containerID)
        docker.APIClient(self.resourceID).stop(containerID)

    def startContainer(self, containerID):
        print("starting container " + containerID)
        docker.APIClient(self.resourceID).start(containerID)

    def killContainer(self, containerID):
        print("Killing container " + containerID)
        docker.APIClient(self.resourceID).kill(containerID)

    def pauseContainer(self, containerID):
        print("Pausing container " + containerID)
        docker.APIClient(self.resourceID).pause(containerID)

    def unpauseContainer(self, containerID):
        print("UnPausing container " + containerID)
        docker.APIClient(self.resourceID).unpause(containerID)

    def restartContainer(self, containerID):
        print("Restarting container " + containerID)
        docker.APIClient(self.resourceID).restart(containerID)
        print('')

    def removeContainer(self, containerID):
        print("Removing container " + containerID)
        docker.api.APIClient(self.resourceID).remove_container(containerID)

    def containerRunningProcesses(self, containerID):
        print("Displaying running processes")
        print(docker.APIClient(self.resourceID).top(containerID))

    def addContainer(self, containerID):
        print("Adding container " + containerID)

    def logprint(self, containerID):
        print("Printing log of " + containerID)
        # print(docker.APIClient(self.resourceID).logs(containerID))
        print("\n")
        return docker.APIClient(self.resourceID).logs(containerID)

    def renameContainer(self, containerID, newName):
        print("renaming container")
        docker.APIClient(self.resourceID).rename(containerID, newName)

    def inspectContainer(self, containerID):
        print("Printing detailed information of " + containerID)
        return docker.APIClient(self.resourceID).inspect_container(containerID)

    def listRunningContainer(self):
        return self.client.containers.list()

    def container_status(self, containerID):
        dictionary = docker.APIClient(self.resourceID).inspect_container(containerID)

        # print(dictionary)
        # print("Mounts " + str(dictionary['Mounts'][0]))
        # print("Mounts " + str(dictionary['Mounts']))
        # # print("Name: " + str(dictionary['Mounts'][0].get('Name')))
        # print("Destination " + str(dictionary['Mounts'][0].get('Destination')))
        #
        # print("Mounts2 " + str(dictionary['Mounts'][1]))
        # print("Source " + str(dictionary['Mounts'][1].get('Source')))
        # print("Destination " + str(dictionary['Mounts'][1].get('Destination')))

        ID = dictionary['Id']
        container_name = dictionary['Name']
        created = dictionary['Created'].rsplit('.', 1)[0]
        start_time = dictionary['State']['StartedAt'].rsplit('.', 1)[0]
        status = dictionary['State']['Status']
        image_name = dictionary['Config']['Image']
        cmd = dictionary['Config']['Cmd']
        env = dictionary['Config']['Env']
        IPAddress = dictionary['NetworkSettings']['Networks']['bridge']['IPAddress']

        try:
            vol_name = dictionary['Mounts'][0].get('Name')
        except IndexError:
            vol_name = None

        try:
            vol_destination = dictionary['Mounts'][0].get('Destination')
        except IndexError:
            vol_destination = None

        try:
            vol_host = dictionary['Mounts'][1].get('Source')

        except IndexError:
            vol_host = None

        try:
            vol_container = dictionary['Mounts'][1].get('Destination')
        except IndexError:
            vol_container = None

        myDictionary = {'ID': ID, 'Created': created, 'Start_time': start_time, 'Status': status,
                        'Image_name': image_name,
                        'Cmd': cmd, 'Env': env, 'IPAddress': IPAddress, 'Container_name': container_name,
                        'Vol_name': vol_name, 'Vol_destination': vol_destination, 'Vol_host': vol_host,
                        'Vol_container': vol_container}
        return myDictionary

    def runningContainer(self):
        totoalContainers = 0
        print("All Running containers")
        for container in self.client.containers.list():
            dictionary = container.attrs
            print(dictionary)
            totoalContainers += 1

            cr = container.attrs.get('Created')

            print('Id ' + container.short_id)
            print('created:  ' + cr.rsplit('.', 1)[0])
            print('Container Name:  ' + container.attrs.get('Name'))
            print('Image id:  ' + container.attrs.get('Image'))
            print('Status:  ' + dictionary['State']['Status'])
            print('Image name:  ' + dictionary['Config']['Image'])

            print('Image name:  ' + dictionary['NetworkSettings']['Networks']['bridge']['IPAddress'])
            # print('Exposed port:  ' + dictionary['ExposedPorts'])
            # print('Host port:  ' + dictionary['NetworkSettings']['Networks']['bridge']['IPAddress'])
            # break
            # print(str(totoalContainers) + '\t' + container.id)
        print("\n")

    def listAllContainers(self):
        return self.client.containers.list(True)
        # mydict = {}
        # totoalContainers = 0
        # # print("All containers")
        # for container in self.client.containers.list(True):
        #     dictionary = container.attrs
        #     # print(dictionary)
        #     totoalContainers += 1
        #     print(str(totoalContainers) + ')')
        #
        #     cr = container.attrs.get('Created')
        #     print('Id ' + container.C)
        #     mydict['Id'] = container.short_id
        #     print('created:  ' + cr.rsplit('.', 1)[0])
        #     mydict['Created'] =  cr.rsplit('.', 1)[0]
        #     print('Container Name:  ' + container.attrs.get('Name'))
        #     mydict['Container Name'] = container.attrs.get('Name')
        #     print('Image id:  ' + container.attrs.get('Image'))
        #     mydict['Image Id'] = container.attrs.get('Image')
        #     print('Status:  ' + dictionary['State']['Status'])
        #     mydict['Status'] = dictionary['State']['Status']
        #     print('Image name:  ' + dictionary['Config']['Image'])
        #     mydict['Image Name'] = dictionary['Config']['Image']
        #     print('IP Address:  ' + dictionary['NetworkSettings']['Networks']['bridge']['IPAddress'])
        #     mydict['IP Address'] = dictionary['NetworkSettings']['Networks']['bridge']['IPAddress']
        #
        # print("\n")

# # #
# con = Container()
# con.calculate_network_IO('15ec352cd1e1')
# con.calculate_disk_usage('15ec352cd1e1')
# con.calculate_memory_percent('15ec352cd1e1')
# print(con.calculate_cpu_percent('15ec352cd1e1'))
#
# con.calculate_network_IO('64ff7546650f')
# con.calculate_disk_usage('64ff7546650f')
# con.calculate_memory_percent('64ff7546650f')
# print(con.calculate_cpu_percent('64ff7546650f'))
# print(con.inspectContainer('15ec352cd1e1'))
# while True:
#
# while True:
#
# con.container_status('9fd5257092ac')
# con.logprint('15ec352cd1e1')
# con.runningContainer()
# print(con.listAllContainers())
