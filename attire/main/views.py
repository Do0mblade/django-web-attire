from django.shortcuts import render, redirect
from .forms import SubscriberForm, NewUserForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def index(request):
    form = SubscriberForm()
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'main/index.html', {'form': form})

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Это имя пользователя уже занято')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Этот email уже используется')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'Вы зарегистрированы и можете войти в систему')
                    return redirect('login')
        else:
            messages.error(request, 'Пароли не совпадают')
            return redirect('register')
    else:
        return render(request, 'main/register.html')

def login_request(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("profile")
            else:
                messages.error(request,"Неверное имя пользователя или пароль.")
        else:
            messages.error(request,"Неверное имя пользователя или пароль.")
    form = LoginForm()
    return render(request=request, template_name="main/login.html", context={"login_form":form})


@login_required
def profile(request):
    return render(request, 'main/profile.html', {'user': request.user})

def logout_view(request):
    logout(request)
    # Перенаправление на главную страницу после выхода
    return redirect('home')