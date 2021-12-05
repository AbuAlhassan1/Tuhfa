"""Tuhfa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from categories.views import categories_controller
from userForm.views import userForm_controller
from posts.views import posts_controller
from adminUser.views import admin_controller
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def index(request):
    return HttpResponse("Plz Enter The Correct URL ( /api/docs/ ) Or (/admin/) -_-")

api = NinjaAPI()
api.add_router('categories', categories_controller)
api.add_router('userForm', userForm_controller)
api.add_router('posts', posts_controller)
api.add_router('admin', admin_controller)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('', index)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
