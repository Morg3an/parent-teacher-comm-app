from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm, MessageForm, MeetingForm
from .models import Message, Meeting, User, Student

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})

class LoginViewCustom(LoginView):
    template_name = "login.html"
    authentication_form = LoginForm

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def dashboard(request):
    if request.user.role == "teacher":
        students = Student.objects.filter(teacher=request.user)
    else:
        students = Student.objects.filter(parent=request.user)
    messages = Message.objects.filter(recipient=request.user).order_by("-sent_at")[:5]
    meetings  = Meeting.objects.filter(created_by=request.user).order_by("-scheduled_for")[:5]
    return render(request, "dashboard.html", locals())

@login_required
def message_create(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        form.instance.sender = request.user
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = MessageForm()
    return render(request, "message_form.html", {"form": form})

@login_required
def meeting_create(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        form.instance.created_by = request.user
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = MeetingForm()
    return render(request, "meeting_form.html", {"form": form})

@login_required
def message_reply(request, msg_id):
    original = Message.objects.get(id=msg_id, recipient=request.user)
    if request.method == "POST":
        form = MessageForm(request.POST)
        form.instance.sender = request.user
        form.instance.recipient = original.sender
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = MessageForm(initial={"recipient": original.sender})
    return render(request, "message_form.html", {"form": form})