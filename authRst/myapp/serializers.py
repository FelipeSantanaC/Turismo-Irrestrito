from rest_framework import serializers 
from myapp.models import MyUser
 
 
class UserSerializer(serializers.ModelSerializer):  

    class Meta:
        model = MyUser
        fields = ('email',
                  'name',
                  'password')