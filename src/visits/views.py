from django.shortcuts import render


def homepage_view(request):
    if request.user.is_authenticated:
        return render(request, "dashboard/main.html")
    context = {
        "page_view_count": 0,
        "social_views_count": 0,
    }
    return render(request, "homepage.html", context)
