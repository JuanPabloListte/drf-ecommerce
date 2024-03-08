from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from apps.users.api.serializers import UserTokenSerializer
from django.contrib.sessions.models import Session
from datetime import datetime
from rest_framework.views import APIView
from django.utils import timezone
from apps.users.authentication_mixins import Authentication


class UserToken(Authentication, APIView):
    def get(self, request, *args, **kwargs):
        
        try:
            user_token,_ = Token.objects.get_or_create(user = self.user)
            user = UserTokenSerializer(self.user)
            return Response({
                'token': user_token.key,
                'user': user.data,
            })
        except:
            return Response({
                'error': 'Invalid credentials sent'
            }, status=status.HTTP_400_BAD_REQUEST)

class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context = {'request':request})
        
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                            'token': token.key,
                            'user': user_serializer.data,
                            'message': 'Login succesfully!'
                    }, status=status.HTTP_201_CREATED)
                else:
                    all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response({
                            'token': token.key,
                            'user': user_serializer.data,
                            'message': 'Login succesfully!'
                    }, status=status.HTTP_201_CREATED)
                    # return Response({
                    #     'error': 'Session already started with this user'
                    # }, status=status.HTTP_409_CONFLICT)
            else:
                return Response({'error': 'This account is inactive'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Login failed. Please check your username and password'}, status=status.HTTP_400_BAD_REQUEST)
    

class Logout(APIView):
    
    def post(self, request, *args, **kwargs):
        try:
            token_key = request.data.get('token')
            if not token_key:
                return Response({'error': 'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)

            token = Token.objects.filter(key=token_key).first()
            if not token:
                return Response({'error': 'Token not found'}, status=status.HTTP_404_NOT_FOUND)
                
            user = token.user
            all_sessions = Session.objects.filter(expire_date__gte=timezone.now())
            if all_sessions.exists():
                for session in all_sessions:
                    session_data = session.get_decoded()
                    if user.id == int(session_data.get('_auth_user_id')):
                        session.delete()
            token.delete()
            session_message = 'User session deleted'
            token_message = 'Token deleted'
            return Response({'token_message': token_message, 'session_message': session_message},
                            status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)