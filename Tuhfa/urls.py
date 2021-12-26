from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from categories.views import categories_controller
from userForm.views import userForm_controller
from posts.views import posts_controller
from adminUser.views import admin_controller
from about.views import about_controller
from schedule.views import schedule_controller
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def index(request):
    return HttpResponse("Plz Enter The Correct URL ( /api/docs ) Or (/admin/) -_-")

api = NinjaAPI()
api.add_router('categories', categories_controller)
api.add_router('userForm', userForm_controller)
api.add_router('posts', posts_controller)
api.add_router('about', about_controller)
api.add_router('admin', admin_controller)
api.add_router('schedule', schedule_controller)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('', index)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)