from django.urls import path
from rest_framework.authtoken import views

from user.views import LoginUserView, CreateUserView, ManageUserView

app_name = "user"


urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", LoginUserView.as_view(), name="login"),
    # path('login/', views.obtain_auth_token, name='login'),
    path("me/", ManageUserView.as_view(), name="manage"),
]
