import docker 
import sys
import os
from api import settings
from shutil import copyfile
from .serializer import SongsSerializer
from .models import Songs
from rest_framework.views import APIView
from django.shortcuts import get_list_or_404, get_object_or_404# Create your views here.
from rest_framework.response import Response

class SongsView(APIView):
    
    def get(self,request):
        '''
            Get request to get any data
        '''
        queryset = Songs.objects.all()
        serializer = SongsSerializer(queryset, many=True)
        return Response({"Songss":serializer.data})


    def post(self,request):
        '''
            This function serialize the data and build the corresponding 
            docker image 
        '''
        queryset = request.data
        serialzer = SongsSerializer(data=queryset)

        if serialzer.is_valid(raise_exception=True):
            status = serialzer.save()

        filename=str(serialzer.instance.uploadFile)
        
        print("file name is "+filename)

        filePath = settings.MEDIA_ROOT+"/"+filename
        copyfile(filePath,os.path.abspath("dockerimages/app.py"))
        client = docker.from_env()
        dockerFilePath = os.path.abspath(os.path.dirname("dockerimages/Dockerfile"))  +"/"
        tagName ="pythonapp"+"_"+str(serialzer.instance.id)
        client.images.build(tag=tagName,path=dockerFilePath)
        
        return Response({"sucess":"Songs '{}' created successfully ".format(str(serialzer.instance.id))})    

    def put(self,request,pk):
        '''
            Function to updated an data
        '''
        saved_article = get_object_or_404(Songs.objects.all(), pk=pk)
        data = request.data
        serializer = SongsSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Song'{}' updated successfully".format(article_saved.title)})

    def delete(self, request, pk):
        '''
            Function to delete any data
        '''
        
        # Get object with this pk
        song = get_object_or_404(Songs.objects.all(), pk=pk)
        song.delete()
        return Response({"message": "Song with id `{}` has been deleted.".format(pk)},status=204)


class DockerContainer(APIView):

    def getStatus(self,cId):

        client = docker.from_env()
        songObject = Songs.objects.get(id=cId)  
        containerName = str(songObject.uploadFile)+"_"+str(cId)
        container =  client.containers.get(containerName) 
        return container.status
   
    def runContainer(self,pk):
        songObject=Songs.objects.get(id=pk)  
        containerName=str(songObject.uploadFile)+"_"+str(pk)
        tagName = "pythonapp_"+str(pk)
        client = docker.from_env()
        return client.containers.run(tagName,name=containerName) 
   
    def post(self,request,pk):
        return Response({"Container Running ":self.runContainer(pk)})

    def get(self,request,pk):
        return Response({"Status":self.getStatus(pk)})
