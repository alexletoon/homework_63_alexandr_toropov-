from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView, ProfileView, UserChangeView, AccountsListView, follow_account

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('follow/<int:pk>/', follow_account, name='follow_account'),
    path('', AccountsListView.as_view(), name='accounts'),
    path('profile/<int:pk>/change/', UserChangeView.as_view(), name='change'),
    path('logout/', logout_view, name='logout')
]
# from django.urls import path



# urlpatterns = [

# ]