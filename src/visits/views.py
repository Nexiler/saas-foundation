from django.shortcuts import render, redirect


def homepage_view(request):
    if request.user.is_authenticated:
        return render(request, "homepage.html")
    else:
        return redirect('account_login')