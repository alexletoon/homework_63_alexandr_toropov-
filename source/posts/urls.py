from django.urls import path

from posts.views import AddPostView, ListPostsView, PostDetailView

urlpatterns = [
    # path('', ListPostsView.as_view(), name='index'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post_detail/<int:pk>', PostDetailView.as_view(), name='post_detail'),



]