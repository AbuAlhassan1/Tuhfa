from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, get_user_model
from Tuhfa.utils.schemas import MessageOut, AdminCreate, AdminOut, AuthOut, SignIn, AdminUpdate, UpdatePassword
from ninja import Router
from .authorization import GlobalAuth, get_user_token
from .models import AdminUser

admin_controller = Router(tags=['admin'])

admin = get_user_model()

# ---------------------------------------------------------------

# SignUp Operation --Start--
@admin_controller.post('signup', response={
    400: MessageOut,
    201: AdminOut,
})
def signup(request, full_name, email, phone, password1, password2):
    if password1 != password2:
        return 400, {
            'detail': 'Passwords do not match !',
        }

    try:
        is_admin_exists = AdminUser.objects.get(email=email)
        
    except AdminUser.DoesNotExist:
        print("dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
        new_admin = AdminUser.objects.create_user(
            full_name=full_name,
            email=email,
            phone=phone,
            password=password1
        )

        token = get_user_token(new_admin)
        return 201, {
            'token': token,
            'admin': new_admin,
        }
    return 400, {
        'detail': 'Email already exists !',
    }

# ---------------------------------------------------------------

# SignIn Operation --Start--
@admin_controller.post('signin')
def signin(request, log_in: SignIn):
    admin = authenticate(
        email=log_in.email,
        password=log_in.password
    )

    if not admin:
        return 404, {
            'detail': 'User Does Not Exist !'
        }

    token = get_user_token(admin)

    return 200, {
        'token': token,
        'admin': admin
    }

# ---------------------------------------------------------------

# Get My Info Operation --Start--
@admin_controller.get('me', auth=GlobalAuth(), response=AdminOut)
def me(request):
    return get_object_or_404(admin, id=request.auth['pk'])

# ---------------------------------------------------------------

# Update Admin Account Operation --Start--
@admin_controller.put('updateAdmin', auth=GlobalAuth(), response={
    200: AdminOut
})
def update_admin(request, update_admin: AdminUpdate):
    admin.objects.filter(id=request.auth['pk']).update(**update_admin.dict())
    return get_object_or_404(admin, id=request.auth['pk'])

# ---------------------------------------------------------------

# Reset Password Operation --Start--
@admin_controller.post('rest-password', auth=GlobalAuth(), response={
    200: MessageOut,
    400: MessageOut
})
def reset_password(request, password_update: UpdatePassword):
    if password_update.password1 != password_update.password2:
        return 400, {
            'detail': 'Passwords do not match !'
        }
    Admin = get_object_or_404(admin, id=request.auth['pk'])
    is_admin = Admin.check_password(password_update.password1)

    if not is_admin:
        return 400, {
            'detail': 'Password is incorrect !'
        }
    
    Admin.set_password(password_update.password1)
    Admin.save()
    return 200, {
        'detail': 'Password has been updated !'
    }

# ---------------------------------------------------------------