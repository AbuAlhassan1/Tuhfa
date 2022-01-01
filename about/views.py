from typing import Any, List
from django.shortcuts import render
from ninja import Router, Form
from ninja.files import UploadedFile
from ninja.params_functions import File
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
    200: List[AboutOut],
    404: MessageOut
})
def retrive_about_section(request):
    try:
        about_info = About.objects.all()
    except:
        return {"message": "There is no about section yet"}

    return about_info

# ---------------------------------------------------------------

# Update An About Section
@about_controller.post("update-about-section", response={
    200: MessageOut,
    404: MessageOut,
    422: MessageOut
})
def update_about_section(request, description: str, image: UploadedFile):
    try:
        about_section = About.objects.first()
    except:
        return {
            'message': "There Is No About Section Yet !!!"
        }
    
    if not about_section:
        return {
            'message': "There Is No About Section Yet !!!"
        }

    try:
        about_section.description = description
        about_section.image = image
        about_section.save()
    except:
        return {
            'message': "SomeThing Went Wrong !!"
        }
    
    return {
        'message': "About Section Updated Successfully"
    }
# ---------------------------------------------------------------