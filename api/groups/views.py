from logging import Manager
from urllib import response
from requests import Response
from rest_framework import generics, status
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer, AddUserToGroupSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class AddUserToGroupView(generics.UpdateAPIView):
    serializer_class = AddUserToGroupSerializer

    def get_object(self):
        group = get_object_or_404(Group, pk=self.kwargs['pk'])
        user_id = self.request.data.get('user_id')
        user = get_object_or_404(User, id=user_id)
        return (user, group)

    def put(self, request, pk):
        user, group = self.get_object()
        user.group = group
        user.save()
        return Response(status=204)


class ListGroupUsersView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        group = get_object_or_404(Group, pk=self.kwargs['pk'])
        return User.objects.filter(group=group)


class DeleteUserFromGroupView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        group = get_object_or_404(Group, pk=self.kwargs['pk'])
        return User.objects.filter(group=group)

    def delete(self, request, pk, user_id):
        user = get_object_or_404(self.get_queryset(), id=user_id)
        user.delete()
        return Response(status=204)
