from rest_framework import serializers
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(slug_field="name", queryset=Group.objects.all(), many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']
        read_only_fields = ['id']


class AddUserToGroupSerializer(serializers.Serializer):
    username = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())
    groups = serializers.SlugRelatedField(slug_field="name", queryset=Group.objects.all(), many=True)

    class Meta:
        fields =['username', 'groups']

class RemoveFromGroupSerializer(serializers.Serializer):
    username = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())
    groups = serializers.SlugRelatedField(slug_field="name", queryset=Group.objects.all(), many=True)

