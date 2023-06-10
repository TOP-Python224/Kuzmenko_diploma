from django.contrib import auth
from django.contrib.auth import logout
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from products.models import Basket
from users.forms import RegisterUserForm, ProfileUserForm, UserLoginForm



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('products:main_page'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'registration/login.html', context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('products:main_page'))


def registerUser(request):
    if request.method == 'POST':
        form = RegisterUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = RegisterUserForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)

# @login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUserForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileUserForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)
    total_sum = sum([basket.sum() for basket in baskets])
    total_quantity = sum([basket.quantity for basket in baskets])

    context = {'form': form, 'baskets': baskets, 'total_sum': total_sum, 'total_quantity': total_quantity}
    return render(request, 'registration/profile.html', context)

