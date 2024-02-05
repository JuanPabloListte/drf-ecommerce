from django.urls import path
from apps.users.api.api import UserApiView

urlpatterns = [
    path('user/', UserApiView.as_view(), name='user_api')
]
