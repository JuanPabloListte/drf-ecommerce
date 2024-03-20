from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users.models import User
from apps.users.api.serializers import CustomTokenObtainPairSerializer, CustomUserSerializer
from django.contrib.auth import authenticate, login
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken



class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh_token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Successful Login'
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid token data'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Incorrect username or password'}, status=status.HTTP_400_BAD_REQUEST)
    
class Logout(GenericAPIView):
    def post(self, request: Request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Session closed successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'This user does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    

# class UserToken(Authentication, APIView):
#     def get(self, request, *args, **kwargs):
        
#         try:
#             user_token,_ = Token.objects.get_or_create(user = self.user)
#             user = UserTokenSerializer(self.user)
#             return Response({
#                 'token': user_token.key,
#                 'user': user.data,
#             })
#         except:
#             return Response({
#                 'error': 'Invalid credentials sent'
#             }, status=status.HTTP_400_BAD_REQUEST)

# class Login(ObtainAuthToken):
    
#     def post(self, request, *args, **kwargs):
#         login_serializer = self.serializer_class(data=request.data, context = {'request':request})
        
#         if login_serializer.is_valid():
#             user = login_serializer.validated_data['user']
#             if user.is_active:
#                 token, created = Token.objects.get_or_create(user=user)
#                 user_serializer = UserTokenSerializer(user)
#                 if created:
#                     return Response({
#                             'token': token.key,
#                             'user': user_serializer.data,
#                             'message': 'Login succesfully!'
#                     }, status=status.HTTP_201_CREATED)
#                 else:
#                     all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
#                     if all_sessions.exists():
#                         for session in all_sessions:
#                             session_data = session.get_decoded()
#                             if user.id == int(session_data.get('_auth_user_id')):
#                                 session.delete()
#                     token.delete()
#                     token = Token.objects.create(user=user)
#                     return Response({
#                             'token': token.key,
#                             'user': user_serializer.data,
#                             'message': 'Login succesfully!'
#                     }, status=status.HTTP_201_CREATED)
#                     # return Response({
#                     #     'error': 'Session already started with this user'
#                     # }, status=status.HTTP_409_CONFLICT)
#             else:
#                 return Response({'error': 'This account is inactive'}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response({'error': 'Login failed. Please check your username and password'}, status=status.HTTP_400_BAD_REQUEST)
    

# class Logout(APIView):
    
#     def post(self, request, *args, **kwargs):
#         try:
#             token_key = request.data.get('token')
#             if not token_key:
#                 return Response({'error': 'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)

#             token = Token.objects.filter(key=token_key).first()
#             if not token:
#                 return Response({'error': 'Token not found'}, status=status.HTTP_404_NOT_FOUND)
                
#             user = token.user
#             all_sessions = Session.objects.filter(expire_date__gte=timezone.now())
#             if all_sessions.exists():
#                 for session in all_sessions:
#                     session_data = session.get_decoded()
#                     if user.id == int(session_data.get('_auth_user_id')):
#                         session.delete()
#             token.delete()
#             session_message = 'User session deleted'
#             token_message = 'Token deleted'
#             return Response({'token_message': token_message, 'session_message': session_message},
#                             status=status.HTTP_200_OK)
        
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)