from words.models import Topic, Word
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'word', 'mean', 'topic', 'level', 'favorite']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'topic', 'level', 'favorite']

# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('name',)
#
# class UserSerializer(serializers.ModelSerializer):
#     groups = GroupSerializer(many=True)
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff', 'groups',)