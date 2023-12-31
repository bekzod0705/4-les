from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .serializers import CarSerializer
from .models import CarModel
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import AdminPermissionClass,StaffPermissionClass
# Create your views here.

# class Create(APIView):
#     def post(self,request):
#         if str(request.user)!='AnonymousUser':
#             if request.user.roles==2:
#                 serializer=CarSerializer(data=request.data)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data)
#                 return Response(serializer.errors)
#         else:
#             return Response({'msg':'for staffs'})
        
# class List(APIView):
#     def get(self,request):
#         print(request.user)
#         if str(request.user)=='AnonymousUser':
#             return Response({'msg':'log in !!'})
#         all=CarModel.objects.filter(isEloctrocar=False)
#         serializer=CarSerializer(all,many=True)
#         return Response(serializer.data)

# class Update(APIView):
#     def patch(self,request,*args,**kwargs):
#         if str(request.user)!='AnonymousUser':
#             if request.user.roles==3:
#                 news=get_object_or_404(CarModel,id=kwargs['car_id'])
#                 serializer=CarSerializer(news,data=request.data,partial=True)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data)
#                 return Response(serializer.errors)
#         else:
#             return Response({'msg':'for admins'})
class Create(generics.CreateAPIView):
    queryset=CarModel.objects.all()
    serializer_class=CarSerializer
    permission_classes=(IsAuthenticated,StaffPermissionClass)

class List(generics.ListAPIView):
    serializer_class=CarSerializer
    permission_classes=(IsAuthenticated,)
    def get_queryset(self):
        return CarModel.objects.filter(isEloctrocar=False)

class Update(generics.RetrieveUpdateDestroyAPIView):
    queryset=CarModel.objects.all()
    serializer_class=CarSerializer
    permission_classes=(IsAuthenticated,AdminPermissionClass)