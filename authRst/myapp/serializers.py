from rest_framework import serializers 
from myapp.models import MyUser , Local

class UserSerializer(serializers.ModelSerializer):  

    class Meta:
        model = MyUser
        fields = ('email',
                  'name',
                  'password')


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = (
        'nome',
        'bairro',
        'cidade',
        'estado',
        'foto_url',
        'tipo',
        'nota',
        'relevancia'
            
        )
