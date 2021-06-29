from django.shortcuts import render
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User, Token
import jwt, datetime


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')
            # return Response({
            #     "message": "User not found"
            # })

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=200),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'subroto', algorithm='HS256').decode('utf-8')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)

        Token.objects.create(code=token, user=user).save()

        response.data = {
            'jwt': token
        }

        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed(detail='Unauthenticated!1', code=401)
        try:
            payload = jwt.decode(token, 'subroto', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!2', code=401)

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        token = request.COOKIES.get('jwt')
        code=response.delete_cookie('jwt')
        print(code)
        token = Token.objects.filter(code=token)
        token.delete()
        response.data = {
            'message': 'sucess'
        }
        return response