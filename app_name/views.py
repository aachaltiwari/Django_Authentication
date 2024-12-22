from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied

# Create your views here.
# class BookView(APIView):

#     def get(self, request):
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many = True)
#         return Response(serializer.data, status = status.HTTP_200_OK)
    
#     def post(self, request):
#         seiralizer = BookSerializer(data = request.data)
#         seiralizer.is_valid(raise_exception = True)
#         seiralizer.save()
#         return Response(seiralizer.data, status = status.HTTP_201_CREATED)



class BookView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]  # this is to make sure that only authenticated users can access this view
    serializer_class = BookSerializer
    
    def get_queryset(self):
        # Filter books to only include those belonging to the authenticated user
        return Book.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.id  # Automatically set the authenticated user
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class BookDetailView(RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'put', 'delete']
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    
    def get_queryset(self):
        """
        Filters books for the authenticated user and a specific book ID as provided in the request path.
        Retrieves the book object for the authenticated user or raises a 404 error.
        """
        book_id = self.kwargs.get('pk')  # Assuming 'pk' is the book ID in the path
        queryset = get_object_or_404(Book, id=book_id, user=self.request.user)
        return [queryset]
            
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)


    def put(self, request, *args, **kwargs):
        """
        Handles PUT requests to update a specific book.
        Ensures only the owner of the book can edit it.
        """
        book = self.get_queryset()[0]  # Retrieve the specific book object
        if book.user != request.user:
            raise PermissionDenied("You do not have permission to edit this book.")
        if book.user.id != request.data.get('user'):
            raise PermissionDenied("You cannot change the owner of the book.")
        
        # Perform update
        serializer = self.get_serializer(book, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
    def delete(self, request, *args, **kwargs):
        """
        Handles DELETE requests to remove a specific book.
        Ensures only the owner of the book can delete it.
        """
        book = self.get_queryset()[0]  # Retrieve the specific book object
        if book.user != request.user:
            raise PermissionDenied("You do not have permission to delete this book.")
        
        # Perform deletion
        book.delete()
        return Response(
            {"detail": "Book deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )