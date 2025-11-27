from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import NurseOnboardForm, NurseLoginForm
from .models import NurseProfile
from django.contrib.auth.decorators import login_required

def nurse_landing(request):
    return render(request, "Nurse/landing.html")

def nurse_onboard(request):
    if request.method == "POST":
        form = NurseOnboardForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            # create user
            user, created = User.objects.get_or_create(username=email, defaults={"email": email})
            if created:
                user.set_password(password)
                user.save()
            else:
                # for demo: if user exists, reset password to provided for easy testing
                user.set_password(password)
                user.save()

            # create or update profile
            profile, _ = NurseProfile.objects.get_or_create(user=user)
            profile.full_name = form.cleaned_data["full_name"]
            profile.phone = form.cleaned_data["phone"]
            profile.experience = form.cleaned_data["experience"]
            if request.FILES.get("certificate"):
                profile.certificate = request.FILES["certificate"]
            profile.approved = False  # admin must approve
            profile.save()

            return redirect("nurse_login")
    else:
        form = NurseOnboardForm()
    return render(request, "Nurse/onboard.html", {"form": form})

def nurse_login(request):
    error = None
    if request.method == "POST":
        form = NurseLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                # After login keep simple — send to landing or nurse dashboard later
                return redirect("nurse_home")
            else:
                error = "Invalid credentials"
    else:
        form = NurseLoginForm()
    return render(request, "Nurse/login.html", {"form": form, "error": error})

@login_required
def nurse_home(request):
    # Get nurse profile if exists
    profile = None
    if hasattr(request.user, "nurse_profile"):
        profile = request.user.nurse_profile

    return render(request, "Nurse/home.html", {"profile": profile})

def nurse_logout(request):
    logout(request)
    return redirect("nurse_landing")
