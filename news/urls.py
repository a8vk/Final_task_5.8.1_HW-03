from django.urls import path
from .views import (
    NewsListView,
    NewDetailView,
    UncosNewsListView,
    ArticlesNewsListView,
    NewsSearchView,
    news_search,

    UncosCreateView,
    UncosUpdateView,
    UncosDeleteView,
    ArticlesCreateView,
    ArticlesUpdateView,
    ArticlesDeleteView,
)

urlpatterns = [
    path('', NewsListView.as_view(template_name='index.html'), name='index'),
    path('<int:pk>/', NewDetailView.as_view(), name='detail'),
    path('uncos/', UncosNewsListView.as_view(), name='uncos'),
    path('articles/', ArticlesNewsListView.as_view(), name='articles'),
    path('news/', NewsSearchView.as_view(), name='news'),
    path('search/', news_search, name='news_search'),

    path('uncos/create/', UncosCreateView.as_view(), name='uncos_create'),
    path('uncos/<int:pk>/edit/', UncosUpdateView.as_view(), name='uncos_edit'),
    path('uncos/<int:pk>/delete/', UncosDeleteView.as_view(), name='uncos_delete'),
    path('articles/create/', ArticlesCreateView.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', ArticlesUpdateView.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete/', ArticlesDeleteView.as_view(), name='articles_delete'),
]
