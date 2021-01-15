from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from words import views

urlpatterns = [
    path('words/', views.WordList.as_view()),
    path('words/<int:pk>/', views.WordDetail.as_view()),
    path('topics/', views.TopicList.as_view()),
    path('topics/<int:pk>/', views.TopicDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)