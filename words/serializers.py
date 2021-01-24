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

class StatListView(ListAPIView):
    queryset = Word.objects.raw("SELECT * FROM")
    serializer_class = WordSerializer

    def list(self):
        queryset = self.get_queryset()
        serializer = WordSerializer(list(queryset), many=True)
        return Response(serializer.data)