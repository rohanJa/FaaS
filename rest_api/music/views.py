from .serializer import SongsSerializer
from .models import Songs
from rest_framework.views import APIView
from django.shortcuts import get_list_or_404, get_object_or_404# Create your views here.

from rest_framework.response import Response

class SongsView(APIView):

    # queryset = Songs.objects.all()
    # serializer_class = SongsSerializer
    
    def get(self,request):
        queryset = Songs.objects.all()
        # print("queryset "+str(queryset))
        serializer = SongsSerializer(queryset, many=True)
        # print("request.data "+str(request))
        # serializer_class = SongsSerializer
        # print(vars(serializer_class.data))
        return Response({"Songss":serializer.data})


    def post(self,request):
        queryset = request.data
        serialzer = SongsSerializer(data=queryset)

        if serialzer.is_valid(raise_exception=True):
            status = serialzer.save()

        return Response({"sucess":"Songs '{}' created successfully ".format(status.title)})    


    def put(self,request,pk):
        saved_article = get_object_or_404(Songs.objects.all(), pk=pk)
        data = request.data
        serializer = SongsSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Song'{}' updated successfully".format(article_saved.title)})

    def delete(self, request, pk):
        # Get object with this pk
        song = get_object_or_404(Songs.objects.all(), pk=pk)
        song.delete()
        return Response({"message": "Song with id `{}` has been deleted.".format(pk)},status=204)

