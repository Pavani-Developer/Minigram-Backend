from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path('registeruser/', views.registerView),
    path('user/<str:username>/', views.getuserView),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/userprofile/update', views.update_profile, name='user-profile-update'),
    path('userdata/<int:id>/', views.user_data, name='user-data'),
    path('create-post',views.createPost, name='user-create-post'),
    path('get-posts',views.get_posts, name='user-get-posts'),
    path('get-post/<int:id>',views.get_single_post, name='user-get-single-post'),

]
#http://127.0.0.1:8000/user/profile/update/