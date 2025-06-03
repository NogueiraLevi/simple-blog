from blog.views import (category, created_by, page, post, tags, 
                        search, PostListView, CreatedByListView) 
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/<slug:slug>/', post, name='post'),
    path('page/<slug:slug>/', page, name='page'),  
    path(
        'created_by/<int:author_pk>/',
        CreatedByListView.as_view(),
        name='created_by'
    ),
    path('category/<slug:slug>/', category, name='category'),
    path('tags/<slug:slug>/', tags, name='tags'),
    path('search/', search, name='search'),
]