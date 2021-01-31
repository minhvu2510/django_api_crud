from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from words import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('words', views.WordList.as_view()),
    path('word/<int:pk>', views.WordDetail.as_view()),
    path('topics', views.TopicList.as_view()),
    path('topic/<int:pk>/', views.TopicDetail.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('word_custom/', views.WordByQuery.as_view()),
    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema')
]

# urlpatterns = format_suffix_patterns(urlpatterns)