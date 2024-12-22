from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import Book


class UserCreateSer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'phone_number']
        
        
        
class UserSer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number']
        
        
class BookSerializer(serializers.ModelSerializer):
    start_vowel = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'user', 'start_vowel']

    def get_start_vowel(self, obj):
        vowels = 'AEIOUaeiou'
        return obj.title[0] in vowels if obj.title else False