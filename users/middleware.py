from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from users.models import User, Token
import jwt
from django.db.models import Q
from django.conf import settings
from django.shortcuts import render, HttpResponse


class Auth(APIView):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, *args, **kwargs):
        view_function = '.'.join((view_func.__module__, view_func.__name__))
        exclusion_set = getattr(settings, 'EXCLUDE_FROM_MY_MIDDLEWARE', set())
        if view_function in exclusion_set:
            return None

        token = request.COOKIES.get('jwt')

        # if not token:
        #     raise AuthenticationFailed('Unauthenticated!1')
        t = request.headers['Authorization'].replace("Bearer ", "")
        try:
            # payload = jwt.decode(token, 'subroto', algorithms=['HS256'])

            decode = jwt.decode(t, 'subroto', algorithms=['HS256'])
            tok = Token.objects.filter(Q(code=t) and Q(user__id=decode['id'])).first()
            print(tok)

            if not tok:
                raise AuthenticationFailed

        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Signature has expired'}, status=401)

        except AuthenticationFailed as e:
            print(e.detail)
            return JsonResponse({'error': e.detail}, status=e.status_code)