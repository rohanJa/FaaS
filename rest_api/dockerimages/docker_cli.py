import docker 
import sys
from shutil import copyfile


# with open(sys.argv[1]) as f:
#     with open("app.py", "w") as f1:
#         for line in f:
#         	# print("hello")
#             f1.write(line)

copyfile(sys.argv[1],"app.py")
client = docker.from_env()
client.images.build(tag="pythonapp3",path="./",)
print(client.containers.run("pythonapp3",name="hello1"))
# print(docker.containers.status)
# client.containers.kill(signal=None)

