from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    ROLE_CHOICES = (
        ("parent", "Parent"),
        ("teacher", "Teacher"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Student(models.Model):
    name   = models.CharField(max_length=100)

    parent  = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'parent'},
        related_name='children'        # unique name
    )

    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'teacher'},
        related_name='students'        # different unique name
    )

    math_score    = models.PositiveIntegerField(default=0)
    english_score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Message(models.Model):
    sender      = models.ForeignKey(User, related_name="sent_msgs", on_delete=models.CASCADE)
    recipient   = models.ForeignKey(User, related_name="recv_msgs", on_delete=models.CASCADE)
    body        = models.TextField()
    sent_at     = models.DateTimeField(default=timezone.now)

class Meeting(models.Model):
    student       = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_by    = models.ForeignKey(User, on_delete=models.CASCADE)
    scheduled_for = models.DateTimeField()
    notes         = models.CharField(max_length=255, blank=True)