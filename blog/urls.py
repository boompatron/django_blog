from django.urls import path
from . import views

urlpatterns = [
    # path('/<int:pk>/', views.single_post_page), # this was FBV
    # path('/', views.index), # this was FBV
    path('/<int:pk>/', views.PostDetail.as_view()),
    path('/', views.PostList.as_view()),
]
