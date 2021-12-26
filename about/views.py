from django.shortcuts import render
from ninja import Router
from ninja.files import UploadedFile
from Tuhfa.utils.schemas import MessageOut, AboutOut
from .models import About

about_controller = Router(tags=["about"])

# ---------------------------------------------------------------

# Create An About Sction
@about_controller.post("create-about-info", response={
    201: AboutOut,
    200: MessageOut,
    500: MessageOut,
    409: MessageOut
})
def create_about_info(request, image: UploadedFile, description: str):
    
    is_there_about_section = About.objects.all()

    if is_there_about_section:
        return {"message": "There is already an about section just update it :)"}

    try:
        abiut_info = About.objects.create(image=image, description=description)
    except:
        return {
            "message": "Somthing Went Wrong While Creating About Section !!!"
        }

    return 201, abiut_info

# ---------------------------------------------------------------

# Retrieve An About Section
@about_controller.get("retrive-about-section", response={
    200: AboutOut,
    404: MessageOut
})
def retrive_about_section(request):
    try:
        about_info = About.objects.get(id=1)
    except:
        return {"message": "There is no about section yet"}

    return 200, about_info

# ---------------------------------------------------------------

# Update An About Section
@about_controller.put("update-about-section", response={
    "200": AboutOut,
    "404": MessageOut
})
def update_about_section(request, image: UploadedFile, description: str):
    try:
        about_info = About.objects.get(id=1)
    except:
        return {"message": "There is no about section yet"}

    try:
        about_info.image = image
        about_info.description = description
        about_info.save()
    except:
        return {"message": "Somthing Went Wrong While Updating About Section !!!"}

    return 200, about_info


# ---------------------------------------------------------------