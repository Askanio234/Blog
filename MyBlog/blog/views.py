from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Author, Blog, Comment
from django.urls import reverse


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


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text', ]

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return super(CommentCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'], })
