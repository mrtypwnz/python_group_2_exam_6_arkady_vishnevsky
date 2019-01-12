from django.urls import path
from webapp.views import ArticleListView, ArticleDetailView,\
    ArticleCreateView, ArticleUpdateView, ArticleDeleteView, UserListView, UserView, UserUpdateView

app_name = 'webapp'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/create', ArticleCreateView.as_view(), name='article_create'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>', UserView.as_view(), name='user_office'),
    path('users/<int:pk>', UserUpdateView.as_view(), name='user_edit')

]

