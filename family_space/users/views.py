from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer


class UserRegisterView(generics.CreateAPIView):
    """
    Регистрация пользователя.
    """
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        user_data = {
            "name": f"{user.last_name} {user.first_name} {user.patronymic}",
            "email": user.email
        }

        return Response({
            "data": {
                "user": user_data,
                "code": 201,
                "message": "Пользователь создан"
            }
        }, status=status.HTTP_201_CREATED)


from rest_framework_simplejwt.views import TokenObtainPairView

class UserLoginView(TokenObtainPairView):
    pass


from rest_framework.authtoken.models import Token
from .serializers import UserAuthSerializer


class UserAuthView(generics.GenericAPIView):
    """
    Аутентификация пользователя.
    """
    serializer_class = UserAuthSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        # Генерация или получение токена
        token, created = Token.objects.get_or_create(user=user)

        user_data = {
            "id": user.id,
            "name": f"{user.first_name} {user.patronymic} {user.last_name}",
            "birth_date": user.birth_date.isoformat(),  # Форматирование даты
            "email": user.email
        }

        return Response({
            "data": {
                "user": user_data,
                "token": token.key
            }
        }, status=status.HTTP_200_OK)
