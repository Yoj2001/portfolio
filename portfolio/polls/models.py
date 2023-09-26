from django.db import models
from django.contrib.auth.models import User


class Programmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    age = models.PositiveIntegerField(blank=False)
    language = models.CharField(max_length=50, blank=False)
    framework = models.CharField(max_length=50, blank=False)
    experience = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Project(models.Model):
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(default="No description")

    def __str__(self):
        return self.name
