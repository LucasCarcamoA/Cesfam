from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect


def admin_required(view_func):
    def check_admin(user):
        return user.is_authenticated and (user.is_staff or user.is_superuser)
    
    decorated_view_func = user_passes_test(check_admin, login_url='/login/')(view_func)
    return decorated_view_func

