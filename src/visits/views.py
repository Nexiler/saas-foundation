from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

LOGIN_URL = settings.LOGIN_URL


def homepage_view(request):
    context = {
        "page_view_count": 0,
        "social_views_count": 0,
    }
    return render(request, "homepage.html", context)


def dashboard_view(request):
    if request.user.is_authenticated:
        return render(request, "dashboard/main.html")
    return redirect("/accounts/login/")


@login_required
def user_only_page_view(request, *args, **kwargs):
    # print(request.user.is_stuff)
    return render(request, "protected/user_only_page.html")


@staff_member_required(login_url=LOGIN_URL)
def staff_only_page_view(request, *args, **kwargs):
    return render(request, "protected/user_only_page.html")
