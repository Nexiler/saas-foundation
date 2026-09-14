from django.shortcuts import render


def homepage_view(request):
    if request.user.is_authenticated:
        return render(request, "dashboard/main.html")
    return render(request, "homepage.html")
