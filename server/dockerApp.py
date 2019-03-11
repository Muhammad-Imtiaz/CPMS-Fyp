from server.myContainer import Container
from server.mySystem import System
from server.myVolume import Volume


containerObj = Container()

containerObj.listAllContainers()
containerObj.listRunningContainer()
# containerObj.dockerstats('cd8b4dadad34a0f8025e2d031df18f92315917aca288625f2dbd1c9e0dfd5033')


# myimage = Image()
# myimage.listAllImages()
#myimage.image_details('89c72b64ab63')

# list = myimage.pullImage('busybox')
# print(list.id)
# myimage.removeImage('hello-world')
# print(myimage.get('busybox').id)
# myimage.image_details('busybox:latest')
# myimage.searchImage('busybox:latest')


mySystem = System()
# mySystem.docker_system_disk_usage()
# mySystem.docker_system_info()
# mySystem.docker_system_events()

myVol = Volume()
myVol.list_volume()
# myVol.inspect_volume('ffa3db06efd95bcb1d0013886f968299df2c1e56636844874c32da8ff442279f')
# myVol.remove_volume('b4e9ce3247b3562b19b73e9eccf6cd838194d1b14b31361587944ded174a84f5')
