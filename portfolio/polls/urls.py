from django.urls import path
from .views import *

app_name = "polls"
urlpatterns = [
    path("", programmers_list, name="index"),
    path("detail/<int:prog_id>", detail, name="detail"),
    path("add_user/", add_user, name="add_user"),
    path("user_save/", user_save, name="user_save"),
    path("add_project/<int:programmer_id>", add_project, name="add_project"),
    path("add_project_page/<int:programmer_id>", add_project_page, name="add_project_page"),
]
