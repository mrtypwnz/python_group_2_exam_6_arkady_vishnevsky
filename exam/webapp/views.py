from django.views.generic import DetailView, CreateView, UpdateView, View, DeleteView, ListView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from webapp.models import UserInfo, Post
from webapp.forms import PostForm

class ArticleListView(ListView):
    model = Post
    template_name = 'post_list.html'

class ArticleDetailView(DetailView):
    pass


class ArticleCreateView(CreateView):
    model = Post
    template_name = 'article_create.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('webapp:article_detail', kwargs={'pk': self.object.pk})

class ArticleUpdateView(UpdateView):
    model = Post
    template_name = 'article_update.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

class ArticleDeleteView(DeleteView):
    pass

class UserListView(ListView):
    model = UserInfo
    template_name = 'user_list.html'

class UserView(View):
    model = UserInfo
    template_name = 'user_office.html'


