from django.urls import path
from app import views

urlpatterns = [
    path('', views.welcome, name='welcome'), 
    path('users/', views.RegisterUserView.as_view(), name='register_user'),
    path('friend_requests/', views.FriendRequestCreateView.as_view(), name='friend_request_create'),
    path('friend_requests/', views.FriendRequestListView.as_view(), name='friend_request_list'),
    path('friend_requests/<int:id>/', views.FriendRequestUpdateView.as_view(), name='friend_request_update'),
    path('friends/', views.FriendListView.as_view(), name='friend_list'),
    path('friend_status/<str:username>/', views.FriendStatusView.as_view(), name='friend_status'),
    path('friends/<str:username>/', views.FriendRemoveView.as_view(), name='friend_remove'),
]
