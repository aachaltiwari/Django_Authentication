from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

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
