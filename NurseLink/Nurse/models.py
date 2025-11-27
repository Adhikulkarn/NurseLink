from django.contrib.auth.models import User
from django.db import models

class NurseProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="nurse_profile")
    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20, blank=True)
    experience = models.PositiveIntegerField(default=0, help_text="Years of experience")
    certificate = models.FileField(upload_to="nurse_certificates/", null=True, blank=True)
    approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} ({self.user.email})"
