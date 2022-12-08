import logging

from hotel.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from django.shortcuts import redirect, render

logger = logging.getLogger(__name__)


def user_login(request):
    if request.user.is_authenticated:
        return render(request, 'authentication/login.html', )
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        logger.info(request, f"Authenticated successfully")
                        return redirect('/', )
                    else:
                        return HttpResponse('Disabled account')
                else:
                    return HttpResponse('Invalid login')
        else:
            form = LoginForm()
        return render(request, 'authentication/login.html', {'form': form})


def logout_view(request):
    if request.method == "GET":
        logout(request)
        return render(request, "authentication/logout.html", )
    return HttpResponse('Success')
