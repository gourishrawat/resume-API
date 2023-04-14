from django.shortcuts import render
from rest_framework.response import Response
from app.models import profile
from app.serializers import profileSerializer
from rest_framework.views import status
from rest_framework.views import APIView

# Create your views here.
class profileview(APIView):
    def post(self,request,format=None):
        serializer= profileSerializer(data=request.dat)
        if serializer .is_valid():
            serializer.save()
            return Response ({'msg':'resume upload sucesssfully','status':'suucess','candidate':serializer.data},
                             status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def get(self, request, formate=None):
        candidate = profile.objects.all()
        serializer = profileSerializer(candidate,many=True)
        return Response ({'status':'sucess','candidate':serializer.data},status=status.HTTP_200_OK)
    
    def delete(self,request,formate=None):
        candidate=profile.objects.all()
        return Response({'status':'success'})
