from django.shortcuts import render
from .models import Author, Blog, Comment


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
