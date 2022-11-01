from re import template
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, ListView
from posts.models import Post
from posts.forms import PostCreationForm
from django.shortcuts import redirect
from django.urls import reverse


class ListPostsView(ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'



class AddPostView(CreateView):
    template_name: str = 'add_post.html'
    model = Post
    form_class = PostCreationForm
    # success_url = '/'


    def post(self, request, *args: str, **kwargs):
        form = self.get_form_class()(request.POST, request.FILES)
        if form.is_valid():
            author = request.user
            description = form.cleaned_data.get('description')
            image = form.cleaned_data.get('image')
            Post.objects.create(author=author, description=description, image=image)
        return redirect('index')



class PostDetailView(DetailView):
    template_name: str = 'post_detail.html'
    model = Post


        # return super().post(request, *args, **kwargs)
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_invalid(form)


    
    # def get_success_url(self) -> str:
    #     return redirect('profile', pk=self.request.user.id)

    
    # def get_success_url(self) -> str:
    #     return reverse(self.request, 'index')
