from rest_framework_simplejwt import authentication
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer, TokenSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# JWT settings
from rest_framework_simplejwt.tokens import RefreshToken

# POST user/login/
class LoginView(generics.ListCreateAPIView):

    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        # print(request.data)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            serializer = TokenSerializer(data={ "token": str(refresh.access_token) })
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


# POST user/signup/
class RegisterUsersView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username or not password or not email:
            return Response(
                data={ "message": "username, password and email is required to register a user" },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(status=status.HTTP_201_CREATED)

class UsersView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return User.objects.filter(username=username);

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_userInfo(request, token):

    jwt_object = authentication.JWTAuthentication()
    validated_token = jwt_object.get_validated_token(token)
    user = jwt_object.get_user(validated_token)

    serializer = UserSerializer(user, many=False)

    print(token)
    print(user)

    return Response(serializer.data)
