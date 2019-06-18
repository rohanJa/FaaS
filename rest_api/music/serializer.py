from rest_framework import serializers
from .models import Songs

class SongsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=20)
    artist = serializers.CharField(max_length=20)
    uploadFile = serializers.FileField()
    # container_id = serializers.IntegerField()    
    
    
    def create(self, validated_data):
        '''
            This method is invoked when save invoked from post.
            Explanation:-
            We will need to implement thecreate method in the 
            serializer that tells the serializer what to do 
            when the serializer save method is invoked.
        '''    
        return Songs.objects.create(**validated_data)


    def update(self,instance,validated_data):
        '''
            This method is called to update.  
            Update method is that we are passing 
            in the instance of the article we want to 
            update and if the user has provided a value to update.
        '''
        instance.title = validated_data.get('title', instance.title)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.uploadFile = validated_data.get('uploadFile', instance.uploadFile)
        instance.save()
        return instance