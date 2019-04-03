import docker


class Image:
    client = docker.from_env()
    resourceID = base_url = 'unix://var/run/docker.sock'

    def image_detail(self, image_name):
        dictionary = docker.APIClient(self.resourceID).inspect_image(image_name)

        id = dictionary['Id']
        created = dictionary['Created']
        size = dictionary['Size']
        cmd = dictionary['ContainerConfig']['Cmd'][3].rsplit(' ', 1)[1]
        entry_point = dictionary['ContainerConfig']['Entrypoint'][0]
        volumes = dictionary['ContainerConfig']['Volumes']
        expose_port = dictionary['ContainerConfig']['ExposedPorts']
        env = dictionary['ContainerConfig']['Env']
        #
        # print(size/(1024*2))
        # print(size)
        # print(entry_point)
        # print(cmd)
        # print(volumes)
        # print(expose_port)
        # print(env)

        myDictionary = {'ID': id, 'Created': created, 'Size': size,
                        'Cmd': cmd, 'Env': env, 'Entry_point' : entry_point,
                        'Vol_name': volumes, 'Expose_ports': expose_port}
        return myDictionary



    def listAllImages(self):
        return docker.APIClient(self.resourceID).images()


    def pullImage(self, repository, auth_config=None, platform=None):
        print('pulling image')
        images = self.client.images.pull(repository)
        return images

    def removeImage(self, imageName, forceRemoval=False, noprune=False):
        self.client.images.remove(imageName, forceRemoval, noprune)
        print("image successfully removed...")

    def pushImage(self, imageName, repository, auth_config, imageTag='', stream=True, decode=True):
        for line in self.client.images.push(imageName + imageTag, repository, stream, decode):
            print(line)
        print("image successfully pushed...")

    def delete_unused(self, filter=None):
        output = self.client.images.prune(filter)
        print(output)

    def get(self, imageID):
        image = self.client.images.get(imageID)
        return image

    def searchImage(self, term):
        images = self.client.images.search(term)
        for image in images:
            print(image)
        print('\n')

#
# img = Image()
# # # # img.listAllImages()jupyter/scipy-notebook:latest
# # img.image_detail('wordpress')
# img.image_detail('sha256:a1dc251941519ee661b262a34c741740bcaee3667804c805c26253b141952b8d')