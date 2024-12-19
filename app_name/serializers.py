from djoser.serializers import UserCreateSerializer, UserSerializer

class UserCreateSer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'phone_number']
        
        
        
class UserSer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number']
        
        
