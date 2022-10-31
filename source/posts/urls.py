from django.urls import path

from posts.views import AddPostView, ListPostsView

urlpatterns = [
    path('', ListPostsView.as_view(), name='index'),
    path('add_post/', AddPostView.as_view(), name='add_post'),



]