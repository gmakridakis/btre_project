from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        email = request.POST["email"]
        
        # Validations
        if password != password2:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "User with the same username already exists")
            return redirect("register")

        user = User.objects.create(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
        user.save()
        auth.login(request, user)
        return(redirect("login"))

    else:
        return render(request, "accounts/register.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=[password])

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")

    else:
        return render(request, "accounts/login.html")

def logout(request):
    return redirect("index")

def dashboard(request):
    return render(request, "accounts/dashboard.html")