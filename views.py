from rest_framework import generics, status
from rest_framework.response import Response
from .models import User, FriendRequest, Friend
from .serializers import UserSerializer, FriendRequestSerializer, FriendSerializer

from django.http import HttpResponse

def welcome(request):
	return HttpResponse("Добро пожаловать!")

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FriendRequestCreateView(generics.CreateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

class FriendRequestListView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        user = self.request.user
        return FriendRequest.objects.filter(models.Q(sender=user) | models.Q(receiver=user))

class FriendRequestUpdateView(generics.UpdateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    lookup_field = 'id'

class FriendListView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return Friend.objects.filter(models.Q(user1=user) | models.Q(user2=user))

class FriendStatusView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(username=self.kwargs['username'])

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
	
    def get(self, request, *args, **kwargs):
        user1 = self.request.user
        username2 = self.kwargs['username']

        try:
            user2 = User.objects.get(username=username2)
        except User.DoesNotExist:
            return Response({"detail": f"User '{username2}' does not exist."},
                            status=status.HTTP_404_NOT_FOUND)

        if FriendRequest.objects.filter(sender=user1, receiver=user2, status="accepted").exists() or \
           FriendRequest.objects.filter(sender=user2, receiver=user1, status="accepted").exists():
            friendship_status = "friends"
        elif FriendRequest.objects.filter(sender=user1, receiver=user2).exists():
            friendship_status = f"{user1.username} sent a friend request to {username2}"
        elif FriendRequest.objects.filter(sender=user2, receiver=user1).exists():
            friendship_status = f"{username2} sent a friend request to {user1.username}"
        else:
            friendship_status = "not friends"
        
        status = "Проверка статуса дружбы"

        return Response({"status": status})

class FriendRemoveView(generics.DestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return Friend.objects.filter(user1=self.request.user, user2__username=self.kwargs['username']) | Friend.objects.filter(user2=self.request.user, user1__username=self.kwargs['username'])

    lookup_field = 'username'

