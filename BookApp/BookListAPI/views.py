from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

@api_view(['POST', 'GET'])
def books(request):
    return Response('List of Books' , status=status.HTTP_200_OK)

class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if(author):
            return Response({"message": 'Books of ' + author} , status=status.HTTP_200_OK)
        return Response({"message": "From Class Methods"} , status=status.HTTP_200_OK)
    def post(self, request):
        title = request.data.get('title')
        if(title):
            return Response({'message': 'Book with Title ' + title} , status=status.HTTP_200_OK)
        return Response({'message': "From Class POST method"}, status=status.HTTP_200_OK)
    
class Book(APIView):
    def get(self, request , pk):
        return Response({"message" : "A Book with id " + str(pk)} , status.HTTP_200_OK)
    def put(self , request, pk):
        return Response({"message" : "Updated Book with id " + request.data.get('title')} , status.HTTP_201_CREATED)


