from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('createpost/', views.CreatePost.as_view(), name = 'createpost'),
    path('updatepost/<int:pk>', views.UpdatePost.as_view(), name = 'updatepost'),
    path('postdetail/<int:pk>', views.PostDetail.as_view(), name = 'postdetail'),
    path('postlike/<int:pk>', views.post_like, name = 'postlike'),
    path('createcomment/<int:pk>', views.create_comment, name = 'createcomment'),
    path('deletepost/<int:pk>', views.DeletePost.as_view(), name = "deletepost"),
    path('draftdetail/<int:pk>', views.DraftDetail.as_view(), name = "draftdetail"),
    path('post_publish/<int:pk>', views.post_publish, name = "post_publish"),

]