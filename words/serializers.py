from words.models import Topic, Word
from rest_framework import serializers
class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'word', 'mean', 'topic', 'level', 'favorite']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'topic', 'level', 'favorite']