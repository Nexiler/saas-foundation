from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

# Create your views here.

User = get_user_model()


@login_required
def profile_detail_view(request, username=None, *args, **kwargs):
    user = request.user

    print(
        user.has_perm("subscriptions.basic"),
        user.has_perm("subscriptions.pro"),
        user.has_perm("subscriptions.advanced"),
    )

    profile_user_obj = get_object_or_404(User, username=username)
    is_me = profile_user_obj == user
    context = {"object": profile_user_obj, "instance": profile_user_obj, "owner": is_me}

    print(f"context:{context}")
    print(f"user:{user}, username:{username}")

    return render(request, "profiles/detail.html", context)
