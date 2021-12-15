from django.shortcuts import render
from rest_framework import authentication
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets

from api import serializers
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated,IsAuthenticatedOrReadOnly,DjangoModelPermissions

# Create your views here.
#[4]VIEW SET
# class StudentViewSet(viewsets.ViewSet):
#     def list(self,request):#list work for getting all the data, work as get method
#         # print("*****LIST*****")
#         # print("Basename:",self.basename)
#         # print("Action:",self.action)
#         # print("Detail:",self.detail)
#         # print("Suffix",self.suffix)
#         # print("Name :",self.name)
#         # print("Discription:",self.description)
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=id):#it provide or get a single record
#         id=pk 
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             http_method_names = ['get', 'post', 'head']

#             return Response(serializer.data)

#     def create(self,request):
#         serializer=StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'}, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def update(self,request,pk):
#         id=pk
#         stu=Student.objects.all(pk=id)
#         serializer=StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def partial_update(self,request,pk):
#         id=pk 
#         stu=Student.objects.get(pk=id)
#         serializer=StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Data Updated'})
#         return Response(serializer.errors)

#     def destroy(self,request,pk):
#         id=pk
#         stu=Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted'})

#[5]MODEL VIEW SET, it is advance version of simple viewset
# class StudentViewSet(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     authentication_classes=[SessionAuthentication]
#     # permission_classes=[DjangoModelPermissions]#provide only get mathod ,not
#     #finded post,update and delete,to get access for post,update and delete method we will 
#     #make changes in user permission in admin page. all the operation will perform when one first login.
#     #but if we want that unauthenticated person can see only data does'nt modify it than we use DjangoModelPermissiionsoranonReadOnly.
#     permission_classes=[DjangoModelPermissionsOrAnonReadOnly]#here also if we login than we can't change , for that we 
    #have to make changes in Admin Page.

    # permission_classes=[IsAuthenticatedOrReadOnly]

    # permission_classes=[IsAuthenticated]

    #if we have to use authentication and permission globally we can make it posssible by writing
    #the below 2 line of codes with some additional code in settings.py
    # authentication_classes=[BasicAuthentication]
    #permission_classes=[IsAuthenticated]
    #permission_classes=[AlowAny], used for allowing wheather user is authenticated or not.
    # permission_classes=[IsAdminUser]

# #READ ONLY MODEL SERIALIZER
# class StudentViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

#[6]Token Authentication
""" we can generte TOKEN BY
(1)add token in admin Application
(2) by cmd
python manage.py drf_create_token username, if token is already generated for the user than will give that token
(3)by exposing an API endpoint
on different termianl:- http POST http://127.0.0.1:8000/gettoken/ username="user1" password="vivek123" 
will provide token if not made earlier and if made earlier than also give the token,after installing httpie
if we want to customise it we can like geeting email,pk etc.
for that we can make another file having auth.py , now in that we will write our required logic for
getting the details and make a post request like as given above request. 
(4)Using Signal->for that we make auth in models specially for creating token at usermaking time.
#Use of httpie:earlier for getting the data we had use browsab;le API but now from cmd/terminal we can use through
on new trminal after installing httpie.(authentication not used)
by typing , http http://127.0.0.1:8000/studentapi/ we will get all the details from database.
(using Authentication)
when we use same request as above from the termianl we will get authorization credentials were not provided, yes it make sense
because hav'nt pass the login detail after applying the above request.
for user1 we use
http http://127.0.0.1:8000/studentapi/ 'Authorization:Token 4bf8f85d81853cafbe34c6c0c13daeef8f6c0f97'
above request will show all the data in the database, with details.
we can also post the data ,user having access to post the data , in our case we have given that freedom to admin and user1
http http://127.0.0.1:8000/studentapi/ name=vivek roll=190 city=Gorakhpur 'Authorization:Token 4bf8f85d81853cafbe34c6c0c13daeef8f6c0f97'
if i am using
permission_classes=[IsAuthenticatedOrReadOnly] as we are unknown user which is not authenticated than we will get all the stored data but we can't modify it(post,put,delete etc). these operation will
work only when we authenticate itself   

"""
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[TokenAuthentication]
<<<<<<< HEAD
    # permission_classes=[IsAuthenticated]     
=======
    permission_classes=[IsAuthenticated]     
>>>>>>> permission
    # permission_classes=[IsAuthenticatedOrReadOnly]     




