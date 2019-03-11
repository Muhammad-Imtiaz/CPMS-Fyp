import docker


class Container:


    client = docker.from_env()
    resourceID = base_url = 'unix://var/run/docker.sock'

    # container = client.containers.run(image='portainer/portainer', detach=True, ports={'9000/tcp': 9092}
    #                                   , name='myPortainerMonitor1',
    #                                   volumes={'/var/run/docker.sock': {'bind': '/var/run/docker.sock'}})

    def dockerstats(self, containerID=None):
        print("Printing stats")
        response = docker.APIClient(self.resourceID).stats(containerID, stream=False)
        print(response['cpu_stats'])
    #
    # def calculateCPUPercentUnix (previousCPU, previousSystemuint64, StatsJSON):
    #     cpuPercent = 0.0
    #     cpuDelta = v.CPUStats.CPUUsage.TotalUsage - previousCPU
    #     pass


    def stream(self):
        for container in self.client.containers.list():
            stats = container.stats(stream=False)
        print(stats)

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
        docker.api.APIClient(containerID).remove_container(containerID)

    def containerRunningProcesses(self, containerID):
        print("Displaying running processes")
        print(docker.APIClient(self.resourceID).top(containerID))

    def addContainer(self, containerID):
        print("Adding container " + containerID)

    def logprint(self, containerID):
        print("Printing log of " + containerID)
        print(docker.APIClient(self.resourceID).logs(containerID))
        print("\n")

    def renameContainer(self, containerID, newName):
        print("renaming container")
        docker.APIClient(self.resourceID).rename(containerID, newName)

    def inspectContainer(self, containerID):
        print("Printing detailed information of " +  containerID)
        print(docker.APIClient(self.resourceID).inspect_container(containerID))


    def listRunningContainer(self):
        return self.client.containers.list()

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


# #
con = Container()
con.dockerstats('4b3fc1b461ec')
con.dockerstats('8b3d488e255c')
# con.runningContainer()
