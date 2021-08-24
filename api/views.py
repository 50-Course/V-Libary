#from django.shortcuts import render
from books.models import Book
from rest_framework import generics
from .serializers import  BookSerializer
# Create your views here.

class BookAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

