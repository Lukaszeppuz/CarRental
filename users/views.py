from django.shortcuts import render, redirect
# from . import forms
from .forms import RegisterUserForm

def register(request):
    if request.method == 'POST':
        form_user_register = RegisterUserForm(request.POST)
        if form_user_register.is_valid():
            form_user_register.save()
            return redirect('login')
        else:
            pas1 = form_user_register.cleaned_data.get('password1')
            pas2 = form_user_register.cleaned_data.get('password2')
            print(pas1, pas2)
            print(form_user_register.error_messages)
    form_user_register = RegisterUserForm()
    context = {'form_user_register': form_user_register}
    return render(request, 'users/register.html.jinja', context=context)

def login(request):
    return render(request, 'users/login.html.jinja')

def logout(request):
    return render(request, 'users/logout.html.jinja')