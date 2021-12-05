from typing import List
from django.shortcuts import get_object_or_404, render
from ninja import Router
from .models import UserForm
from categories.models import Category, Theme
from Tuhfa.utils.schemas import CategorySchema, ThemeSchema, UserCreate, MessageOut, UserOut

userForm_controller = Router(tags=['userForm'])


# ---------------------------------------------------------------

# Create User From --start--
@userForm_controller.post('user', response={
    201: UserOut,
    400: MessageOut
})
def create_user_form(request, categoryId, themeId, fullname, email, phone):
    try:
        category = get_object_or_404(Category, id= categoryId)
        theme = get_object_or_404(Theme, id= themeId)
    except:
        return 404, {'message': 'Category or Theme or Art not found'}

    try:
        user = UserForm.objects.create(full_name=fullname, email=email, phone=phone, category=category, theme=theme)
    except:
        return 400, {'message': 'UserForm not created'}

    return 201, user

# ---------------------------------------------------------------

# Get UserForm By Id --start--
@userForm_controller.get('user/{id}', response={
    200: UserOut,
    404: MessageOut
})
def get_user_form_by_id(request, id):
    try:
        user = UserForm.objects.get(id=id)
    except:
        return 404, { 'message': 'User Not Found !!!' }

    return 200, user

# ---------------------------------------------------------------

# Get All UserForm --start--
@userForm_controller.get('user', response={
    200: List[UserOut],
    404: MessageOut
})
def get_all_user_forms(request):
    try:
        users = UserForm.objects.all()
    except:
        return 404, { 'message': 'User Not Found !!!' }

    return 200, users

# ---------------------------------------------------------------

# Update UserForm By Id --start--
@userForm_controller.put('user/{id}', response={
    200: UserCreate,
    404: MessageOut
})
def update_user_form(request, id, input: UserCreate):
    try:
        user = UserForm.objects.get(id=id)
    except:
        return 404, { 'message': 'User Not Found !!!' }

    user.full_name = input.full_name
    user.email = input.email
    user.phone = input.phone
    user.save()

    return 200, user

# ---------------------------------------------------------------

# Delete UserForm By Id --start--
@userForm_controller.delete('user/{id}', response={
    200: MessageOut,
    404: MessageOut
})
def delete_user_form(request, id):
    try:
        user = UserForm.objects.get(id=id)
    except:
        return 404, { 'message': 'User Not Found !!!' }

    user.delete()

    return 200, { 'message': 'User Deleted !!!' }

# ---------------------------------------------------------------