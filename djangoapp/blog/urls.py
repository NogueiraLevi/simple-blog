from blog.views import (CategoryListView, CreatedByListView, PageDetailView,
                        PostDetailView, PostListView, SearchListView,
                        TagListView)
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/<slug:slug>/', PostListView.as_view(), name='post'),
    path('page/<slug:slug>/', PageDetailView.as_view(), name='page'),  
    path(
        'created_by/<int:author_pk>/',
        CreatedByListView.as_view(),
        name='created_by'
    ),
    path('category/<slug:slug>/', CategoryListView.as_view(), name='category'),
    path('tags/<slug:slug>/', TagListView.as_view(), name='tags'),
    path('search/', SearchListView.as_view(), name='search'),
]