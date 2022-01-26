from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('timeline/<slug>/', views.UserDetailView.as_view(), name='user_detail'),
    path('all/', views.UserListView.as_view(), name='users'),
    path('update/profile/<slug>/', views.UserUpdateView.as_view(), name='user_update'),
    path('delete/profile/<slug>/', views.UserDeleteView.as_view(), name='user_delete'),
]