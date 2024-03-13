from rest_framework import viewsets
from apps.users.api.serializers import UserSerializer, UserListSerializer, UpdateUserSerializer, PasswordSerializer
from apps.users.models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 
from rest_framework import status
from rest_framework.decorators import action


class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer
    queryset = None
    
    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)
    
    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.filter(is_active=True).\
                            values('id', 'username', 'email', 'name')
        return self.queryset
    
    def list(self, request):
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Registration Errors Detected',
                         'errors': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)

    def update(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = UpdateUserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message': 'User updated successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'There are errors updating the user',
                         'errors': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        user_destroy = self.model.objects.filter(id=pk).update(is_active=False)
        if user_destroy == 1:
            return Response({'message': 'User deleted successfully'})
        return Response({'message':'User not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['POST'])
    def set_password(self, request, pk=None):
        user = self.get_object(pk)
        password_serializer = PasswordSerializer(data=request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid password',
                         'errors': password_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def user_api_view(request):
    
#     if request.method == 'GET':
#         users = User.objects.all().values('id', 'username', 'email', 'password')
#         user_serializer = UserListSerializer(users, many=True)
        
#         return Response(user_serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
#         user_serializer = UserSerializer(data=request.data)
        
#         if user_serializer.is_valid():
#             user_serializer.save()
#             return Response({'message':'User created successfully'}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
# @api_view(['GET', 'PUT', 'DELETE'])
# def user_detail_view(request, pk=None):
    
#     user = User.objects.filter(id = pk).first()
    
#     if user:
#         if request.method == 'GET':
#             user_serializer = UserSerializer(user)
#             return Response(user_serializer.data, status=status.HTTP_200_OK)
        
#         elif request.method == 'PUT':
#             user_serializer = UserSerializer(user, data=request.data)
            
#             if user_serializer.is_valid():
#                 user_serializer.save()
#                 return Response(user_serializer.data, status=status.HTTP_200_OK)
#             return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         elif request.method == 'DELETE':
#             user = User.objects.filter(id = pk).first()
#             user.delete()
#             return Response({'message':'Delete successfully'}, status=status.HTTP_204_NO_CONTENT)
    
#     return Response({'message':'User not found'}, status=status.HTTP_404_NOT_FOUND)


