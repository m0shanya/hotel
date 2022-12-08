import logging

from hotel.forms import RegisterForm
from django.contrib.auth.models import User
from django.http import HttpResponse


from django.shortcuts import redirect, render

logger = logging.getLogger(__name__)


def register(request):
    if request.user.is_authenticated:
        return render(request, 'authentication/login.html', )
    else:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                # Process validated data
                logger.info(form.cleaned_data)
                user = User(
                    username=form.cleaned_data["username"],
                    email=form.cleaned_data["email"],
                    first_name=form.cleaned_data["first_name"],
                    last_name=form.cleaned_data["last_name"],
                )
                user.set_password(form.cleaned_data["password"])
                user.save()
                return redirect("/login/")
        else:
            form = RegisterForm()
        return render(request, "reg/registration.html", {"form": form})
