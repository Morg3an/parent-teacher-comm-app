from django.contrib import admin
from django.urls import path, include
from comm import views as v

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", v.signup_view, name="signup"),
    path("login/", v.LoginViewCustom.as_view(), name="login"),
    path("logout/", v.logout_view, name="logout"),
    path("", v.dashboard, name="dashboard"),
    path("message/", v.message_create, name="message_create"),
    path("meetings/new/", v.meeting_create, name="meeting_create"),
    path("message/reply/<int:msg_id>/", v.message_reply, name="message_reply"),

]