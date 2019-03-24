import docker


class Image:
    client = docker.from_env()

    def listAllImages(self):
        return self.client.images.list()

        # totalImages = 0
        # print("Listing all images")
        # for image in self.client.images.list():
        #     totalImages += 1
        #     print(str(totalImages) + '\t' + image.id)
        # print('\n')

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
