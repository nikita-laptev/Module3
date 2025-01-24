from django.contrib.auth.models import User
from rest_framework import serializers
import re

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'patronymic', 'email', 'password', 'birth_date']

    def validate_first_name(self, value):
        if not value.istitle():
            raise serializers.ValidationError("Первая буква должна быть в верхнем регистре")
        return value

    def validate_last_name(self, value):
        if not value.istitle():
            raise serializers.ValidationError("Первая буква должна быть в верхнем регистре")
        return value

    def validate_patronymic(self, value):
        if not value.istitle():
            raise serializers.ValidationError("Первая буква должна быть в верхнем регистре")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Этот email уже зарегистрирован")
        return value

    def validate_password(self, value):
        if len(value) < 3 or not re.search(r"[A-Z]", value) or not re.search(r"[a-z]", value) or not re.search(r"\d", value):
            raise serializers.ValidationError("Пароль должен содержать минимум 3 символа, включать заглавные и строчные буквы, а также цифры")
        return value

    def create(self, validated_data):
        user = User(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            patronymic=validated_data["patronymic"],
            email=validated_data["email"],
        )
        user.set_password(validated_data['password'])  # Хеширование пароля
        user.save()
        return user

from django.contrib.auth import authenticate

class UserAuthSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError("Неправильные логин или пароль")
        attrs['user'] = user
        return attrs
