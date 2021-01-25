from words.models import Word, Topic
from words.serializers import TopicSerializer, WordSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
from rest_framework import permissions
# from django.contrib.auth import authentication
from rest_framework import authentication

class WordList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['topic', 'level']
    # permission_classes = (IsAuthenticated,permissions.IsAuthenticatedOrReadOnly)

    # authentication_classes = [authentication.SessionAuthentication,
    #                           authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['level', 'word']
    # ordering = ['level']

    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = '__all__'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
class WordDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    # IsAuthenticatedOrReadOnly

    # permission_classes = (IsAuthenticated)
    # permission_classes = (DjangoModelPermissionsOrAnonReadOnly)
    # authentication_classes = [authentication.SessionAuthentication,
    #                           authentication.TokenAuthentication]
    # authentication_classes = [authentication.SessionAuthentication,
    #                           authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
class TopicList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TopicDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class WordByQuery(APIView):
    def get(self, request, format=None):
        level = request.GET.get('level', None)
        topic = request.GET.get('topic', None)
        if level and topic:
            snippets = Word.objects.raw('SELECT * FROM words_word WHERE level>%s AND topic=%s',[9,topic])
        else:
            if topic:
                snippets = Word.objects.raw('SELECT * FROM words_word WHERE topic=%s', [topic])
            elif level:
                snippets = Word.objects.raw('SELECT * FROM words_word WHERE level>%s', [level])
            else:
                snippets = Word.objects.raw('SELECT * FROM words_word')
        serializer = WordSerializer(snippets, many=True)
        return Response(serializer.data)
