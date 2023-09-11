from rest_framework import serializers

from .models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class UserRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        max_length=100, write_only=True
    )
    password2 = serializers.CharField(
        max_length=100, write_only=True
    )
    class Meta:
        model = User
        fields = ('id',  'username', 'email', 
                  'number', 'created','password1', 'password2'
                  )
    
    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({'password':'Пароли отличаются'})
        elif attrs['username'] == attrs['password1']:
            raise serializers.ValidationError({'password':'Введённый пароль слишком похож на имя пользователя.'})
        elif len(attrs['password1']) < 8:
            raise serializers.ValidationError({'password':'Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.'})
        elif 'qwertyui' in attrs['password1'] and '12345678' in attrs['password'] and '87654321' in attrs['password']:
            raise serializers.ValidationError({'password':'Введённый пароль слишком широко распространён. (123, qwertyui, 12345678)'})


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'], phone_number=validated_data['number'],
            email=validated_data['email'], 
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'number',
                  'created')