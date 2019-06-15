from rest_framework import serializers
from .models import Songs

class SongsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=20)
    artist = serializers.CharField(max_length=20)
    uploadFile = serializers.FileField()
    # container_id = serializers.IntegerField()    
    
    
    def create(self, validated_data):
        return Songs.objects.create(**validated_data)


    def update(self,instance,validated_data):
        print("instance value is "+str(instance))
        instance.title = validated_data.get('title', instance.title)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.uploadFile = validated_data.get('uploadFile', instance.uploadFile)
        print("validated data "+str(validated_data))
        print("instance.title instance.artist instance.uploadFile " +str(instance.title)+" "+ str(instance.artist)+" "+str( instance.uploadFile))
        instance.save()
        return instance