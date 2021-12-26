from django.shortcuts import get_object_or_404, render
from typing import List
import datetime
from ninja import Router
from pydantic.types import FilePath
from .models import Category, Theme
from Tuhfa.utils.schemas import CategoryIn, MessageOut, CategoryOut, ThemeOut
from ninja.files import UploadedFile

categories_controller = Router(tags=['categories'])

# ---------------------------------------------------------------

# Create Category
@categories_controller.post('create_category', response={
    201: CategoryOut,
    500: MessageOut
})
def create_category(request, name:str, description: str, parent: int = None, image: UploadedFile = None):
    try:
        categories = Category.objects.create(name=name, description=description, parent=parent, image=image)
    except:
        return 500, { 'message': 'Something Went Rong !! :(' }

    return 201, categories

# endpoint consumes file
 
# ---------------------------------------------------------------

# Retrive Category By Id
@categories_controller.get('get_category_by_id', response={
    200: CategoryOut
})
def retrive_category_by_id(request, id):
    categories = get_object_or_404(Category, id=id)
    # categories = Category.objects.select_related().get(id=id) # For Testing Purpose !!!
    return categories

# ---------------------------------------------------------------

# Retrive All Categories
@categories_controller.get('get_all_categories', response={
    200: List[CategoryOut]
})
def retrive_all_categories(request):
    categories = Category.objects.all()
    return categories

# ---------------------------------------------------------------

# Update Category By Id
@categories_controller.put('update_category_by_id', response={
    200: CategoryOut,
    500: MessageOut
})
def update_category_by_id(request, id, input: CategoryIn):
    category = get_object_or_404(Category, id=id)
    category.name = input.name
    category.description = input.description
    if category.id != input.parent:
        category.parent = input.parent
    else:
        return 500, { 'message': "You Can't Assign The ParentId To It Self !!" }
    
    category.save()
    return 200, category

# ---------------------------------------------------------------

# Delete Category By Id
@categories_controller.delete('delete_category_by_id', response={
    200: MessageOut
})
def delete_category_by_id(request, id):
    categories = get_object_or_404(Category, id=id)
    categories.delete()
    return {
        'message': 'Category Deleted Successfully'
    }


# ---------------------------------------------------------------
# ---------------------------------------------------------------
# ---------------------------------------------------------------


# Create Theme
@categories_controller.post('create_theme', response={
    201: ThemeOut,
    500: MessageOut,
    404: MessageOut
})
def create_theme(request, name: str, title: str,description: str, categoryId: int, date: datetime.datetime):
    try:
        category = get_object_or_404(Category, id=categoryId)
        theme = Theme.objects.create(name=name, title=title,description=description, category=category, date=date)
    except:
        return 500, { 'message': str(category) }

    return 201, theme

# ---------------------------------------------------------------

# Get All Themes
@categories_controller.get('get_all_themes', response={
    200: List[ThemeOut]
})
def get_all_themes(request):
    themes = Theme.objects.all()
    return themes

# ---------------------------------------------------------------

# Get Theme By Id
@categories_controller.get('get_theme_by_id', response={
    200: ThemeOut
})
def get_theme_by_id(request, id):
    theme = get_object_or_404(Theme, id=id)
    return theme

# ---------------------------------------------------------------

# Get Themes By Date
@categories_controller.get('get_themes_by_date', response={
    200: List[ThemeOut],
    404: MessageOut
})
def get_themes_by_date(request, date: str):
    themes = Theme.objects.filter(date__icontains=date)
    if not themes:
        return 404, { 'message': 'No Themes Found' }
    return themes

# ---------------------------------------------------------------

# Get Theme By Categoty Name
@categories_controller.get('get_theme_by_category_name', response={
    200: List[ThemeOut]
})
def get_theme_by_category_name(request, name):
    theme = Theme.objects.filter(category__name=name)
    return theme

# ---------------------------------------------------------------

# Get All Themes By Category Id
@categories_controller.get('get_all_themes_by_category_id', response={
    200: List[ThemeOut],
    404: MessageOut
})
def get_all_themes_by_category_id(request, id):
    theme = Theme.objects.filter(category__id=id)
    
    if not theme:
        return 404, { 'message': 'Category Not Found' }

    return theme

# ---------------------------------------------------------------

# Update Theme By Id
@categories_controller.put('update_theme_by_id', response={
    200: ThemeOut,
    500: MessageOut,
    404: MessageOut
})
def update_theme_by_id(request, id, name: str, description: str, categoryId: int):
    try:
        category = get_object_or_404(Category, id=categoryId)
    except:
        return 404, { 'message': 'Category Not Found' }
    
    try:
        theme = Theme.objects.get(id=id)
        theme.name = name
        theme.description = description
        theme.category = category
        theme.save()
    except:
        return 404, { 'message': 'Theme Not Found' }
    
    return 200, theme

# ---------------------------------------------------------------

# Delete Theme By Id
@categories_controller.delete('delete_theme_by_id', response={
    200: MessageOut
})
def delete_theme_by_id(request, id):
    theme = get_object_or_404(Theme, id=id)
    theme.delete()
    return {
        'message': 'Theme Deleted Successfully'
    }

# ---------------------------------------------------------------



