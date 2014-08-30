from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from tmangular.api.filters import IsOwnerFilterBackend
from tmangular.api.serializers import UserSerializer


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    authentication_classes = (JSONWebTokenAuthentication,)
    filter_backend = IsOwnerFilterBackend
    queryset = get_user_model().objects.all()
