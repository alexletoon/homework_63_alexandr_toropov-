from re import template
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, ListView
from django.db.models import Q
from urllib.parse import urlencode
from accounts.forms import LoginForm, CustomUserCreationForm, UserChangeForm, SearchForm
from accounts.models import Account



class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        next = request.GET.get('next')
        form_data = {} if not next else {'next': next}
        form = self.form(form_data)
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        next = form.cleaned_data.get('next')
        user = authenticate(request, email=email, password=password)
        if not user:
            return redirect('login')
        login(request, user)
        if next:
            return redirect(next)
        # return redirect('profile', kwargs={'pk': self.object.pk})
        return redirect('profile', pk= user.id)


def logout_view(request):
    logout(request)
    return redirect('index')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile', pk=user.id)
        context = {}
        context['form'] = form
        return self.render_to_response(context)


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 5
    paginate_related_orphans = 0



    # def get_search_value(self):
    #     if self.form.is_valid():
    #         return self.form.cleaned_data.get('search')
    #     return None


    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     if self.search_value:
    #         query = Q(username__icontains=self.search_value) | Q(email__icontains=self.search_value) | Q(first_name__icontains=self.search_value) 
    #         print(query.__dict__)
    #         queryset = queryset.filter(query)
    #     return queryset


    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(ProfileView, self).get_context_data(object_list=object_list, **kwargs)
    #     context['form'] = self.form
    #     if self.search_value:
    #         context['query'] = urlencode({'search': self.search_value})
    #     return context


class UserChangeView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})
 

class AccountsListView(ListView):
    template_name: str = 'accounts.html'
    context_object_name = 'accounts'
    queryset = Account.objects.all()
    paginate_by: int = 3
    paginate_orphans: int = 1




def follow_account(request, pk):
    user = request.user
    subscribtion = Account.objects.get(id=pk)
    user.subscriptions.add(subscribtion)
    return redirect('profile', pk= user.id)


