from django.views.generic import DetailView, CreateView, UpdateView, View, DeleteView, ListView, TemplateView
from django.urls import reverse, reverse_lazy
from webapp.models import UserInfo, Post
from webapp.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404


class ArticleListView(ListView):
    model = Post
    template_name = 'article_list.html'

    def get_queryset(self):
        return super().get_queryset().order_by('-article_date')

class ArticleDetailView(DetailView):
    pass


class ArticleCreateView(CreateView):
    model = Post
    template_name = 'article_create.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        redirect('webapp:article_list')



class ArticleUpdateView(UpdateView):
    class PostUpdateView(LoginRequiredMixin, UpdateView):
        model = Post
        template_name = 'article_update.html'
        form_class = PostForm

    def get_success_url(self):
        return reverse('webapp:article_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        if self.request.user == post.author:
            return super(ArticleUpdateView, self).dispatch(request, *args, **kwargs)
        elif self.request.user.is_anonymous:
            return redirect('accounts:login')
        else:
            return redirect('webapp:article_detail', pk=kwargs['pk'])

class ArticleDeleteView(DeleteView):
    pass

class UserListView(ListView):
    model = UserInfo
    template_name = 'user_list.html'



class UserView(TemplateView, LoginRequiredMixin):
    template_name = "user_office.html"

    def dispatch(self, request, *args, **kwargs):
        if not UserInfo.objects.filter(user=request.user).exists():
            return redirect(reverse("edit_profile"))
        context = {
            'selected_user': request.user
        }
        return render(request, self.template_name, context)

class UserUpdateView(UpdateView):
    pass


