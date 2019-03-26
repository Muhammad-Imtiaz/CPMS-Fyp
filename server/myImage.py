import docker


class Image:
    client = docker.from_env()
    resourceID = base_url = 'unix://var/run/docker.sock'

    def detail(self):
        pass


    def listAllImages(self):
        return docker.APIClient(self.resourceID).images()
        # print(dictionary)
        # id = dictionary['Id']
        # tags = dictionary['RepoTags']
        # size = str(dictionary['Size']/1024)
        # created = dictionary['Created'].rsplit('.', 1)[0]
        # image_detail = {'Id': id, 'Tags': tags, 'Size': size, 'Created': created}
        # print(image_detail)
        # return image_detail

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

    def image_details(self, image_name):
        image = self.client.images.get(image_name)
        print(image.attrs)

img = Image()
img.listAllImages()