from django.urls import path
from .views import login_view, upload_csv, register_view

urlpatterns = [
    path("register/", register_view),
    path("login/", login_view),
    path("upload_csv/", upload_csv),
]
