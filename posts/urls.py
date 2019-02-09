from django.urls import path
from . import views
from . views import PostListView


urlpatterns = [
    path('blog/', PostListView.as_view(), name='post'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('about/', views.about, name='blog-about'),
]