from datetime import datetime
import json
from rest_framework import generics, permissions, viewsets, mixins
from ..models import myUser,book , Author, transaction
from .serializers import Userserializer, Authorserializer, bs, bookuser, ts
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserListView(generics.ListAPIView):
    queryset = myUser.objects.all()
    serializer_class = Userserializer
  

class UserDetailView(generics.RetrieveAPIView):
    queryset= myUser.objects.all()
    serializer_class = Userserializer


from django.http import Http404

class bookauthor(APIView):
    
    def get_object(self, pk):
        try:
           bk =  Author.objects.get(pk = pk)
           return bk
            
        except book.DoesNotExist:
              raise Http404
    def get(self,request, pk ):
        bk = self.get_object(pk)
       
        serializer = Authorserializer(bk)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request,pk):
        bk = self.get_object(pk)
        s = Authorserializer(bk,data = request.data)
        if s.is_valid():
            s.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response("not Modified",status = status.HTTP_304_NOT_MODIFIED)            

    def delete(self,request,pk):
        bk = self.get_object(pk)
        bk.delete()


class bookauthorlist(APIView):
       
    def get(self,request):
       
        book_list = Author.objects.all()
        serializer = Authorserializer(book_list, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):    
        serializer = Authorserializer( data= request.data)       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)


class bookuser(APIView):
    
    def get_object(self, pk):
        try:
           bk =  book.objects.get(pk = pk)
           return bk        
        except book.DoesNotExist:
              raise Http404
    def get(self,request, pk ):
        bk = self.get_object(pk)       
        serializer = bs(bk)
        return Response(serializer.data, status=status.HTTP_200_OK)
       
    def put(self, request,pk):
        bk = self.get_object(pk)
        s = bs(bk,data = request.data)
        if s.is_valid():
            s.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response("Not Modified",status = status.HTTP_304_NOT_MODIFIED)            

    def delete(self,request,pk):
        bk = self.get_object(pk)
        bk.delete()

from rest_framework.pagination import PageNumberPagination
class bookuserlist(APIView, PageNumberPagination):
     
    def get(self,request):
       
        book_list = book.objects.all()
        result = self.paginate_queryset(book_list,request,view=self )
        serializer = bs(result, many = True)
        return self.get_paginated_response(serializer.data)#, status=status.HTTP_200_OK)

    def post(self, request):

    
        serializer = bs( data= request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)
    
class maketransaction(APIView, PageNumberPagination):
     
    def get(self,request):
       
        transactions = transaction.objects.all()
        transactions_pagination = self.paginate_queryset(transactions, request)
        serializer = ts(transactions_pagination, many = True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
       
        received_data = json.loads(request.body)
        
        return_date = datetime.strptime(received_data['Return_Date'], "%d/%m/%y")
        del received_data['Return_Date']
        received_data['return_date'] = return_date.isoformat()
        json_data = json.dumps(received_data, indent=1)
        print(json_data,"____________json data _____________________")

        serializer = ts( data= json_data)

       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        print("____________validation failed_____________________________")
        return Response(status = status.HTTP_400_BAD_REQUEST)

    

    