from django.shortcuts import render
from .models import Author, Blog, Comment
from django.views import generic


# Create your views here.
def index(request):
    num_bloggers = Author.objects.all().count()
    num_posts = Blog.objects.all().count()
    num_comments = Comment.objects.all().count()
    return render(request, 'index.html', context={
                                        'num_bloggers': num_bloggers,
                                        'num_posts': num_posts,
                                        'num_comments': num_comments
                                        },)


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5


class AuthorListView(generic.ListView):
    model = Author


class BlogDetailView(generic.DetailView):
    model = Blog
