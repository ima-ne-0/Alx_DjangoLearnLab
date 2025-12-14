# posts/views.py
from rest_framework import viewsets, generics, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']  # Enables search functionality

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
class FeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    def get_queryset(self):
        # Get the list of users the current user is following
        following_users = self.request.user.following.all()
        # Filter posts where the author is in that list, ordered by creation date
        return Post.objects.filter(author__in=following_users).order_by('-created_at')