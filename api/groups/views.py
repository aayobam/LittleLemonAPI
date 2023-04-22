from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from api.common.permissions import ManagerPermission
from .serializers import UserSerializer, GroupSerializer, AddUserToGroupSerializer, RemoveFromGroupSerializer


class UserListView(generics.ListAPIView):
    """
    Fetch user records.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [ManagerPermission]


class GroupListCreateView(generics.ListCreateAPIView):
    """
    Fetch and create groups.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [ManagerPermission]

    def perform_create(self, serializer):
        serializer.save()


class AddUserToGroupView(generics.CreateAPIView):
    """
    Adds users to groups.
    """
    queryset = User.objects.all()
    serializer_class = AddUserToGroupSerializer
    permission_classes = [ManagerPermission]

    def get(self, request):
        response = self.queryset.all()
        serializer = UserSerializer(response, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username', None)
        groups = serializer.validated_data.get('groups', [])
        user_obj = User.objects.get(username=username)
        for group in groups:
            if user_obj.groups.filter(name=group).exists():
                return Response({"message": f"{user_obj} already exist in the {group} group"})
            user_obj.groups.add(group)
        response_data = {
            "success":True,
            "message": f"{user_obj} added to the {group} group successfull",
            "data":serializer.data 
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class RemoveUserFromGroupView(generics.GenericAPIView):
    """
    Removes user from group.
    """
    queryset = User.objects.all()
    serializer_class = RemoveFromGroupSerializer
    permission_classes = [ManagerPermission]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username', None)
        groups = serializer.validated_data.get('groups', [])
        user_obj = User.objects.get(username=username)
        for group in groups:
            if not user_obj.groups.filter(name=group).exists():
                return Response({"message": f"{user_obj} is not in the {group} group"})
            user_obj.groups.remove(group)
        response_data = {
            "success":True,
            "message": f"{user_obj} removed from the {group} group successfull",
            "data":serializer.data 
        }
        return Response(response_data, status=status.HTTP_200_OK)

