from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blogs/$', views.BlogListView.as_view(), name='blogs'),
    url(r'^bloggers/$', views.AuthorListView.as_view(), name='bloggers'),
    url(r'^blogs/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
    url(r'^blogs/(?P<pk>\d+)/comment/$', views.CommentCreate.as_view(), name='comment_create'),
]