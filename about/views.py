from typing import List
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
@about_controller.put("update-about-section", response={
    200: AboutOut,
    404: MessageOut
})
def update_about_section(request,description: str, id: int, image: UploadedFile):
    # image = ImageForm(request.POST, request.FILES)

    try:
        update_about_info = About.objects.filter(id=id).update(description=description, image=image)
    except:
        return {"message": "Somthing Went Wrong While Updating About Section !!!"}

    if update_about_info:
        about_info = About.objects.get(id=id)
        return 200, about_info
    else:
        return {"message": "Somthing Went Wrong While Updating About Section !!!"}
    

# ---------------------------------------------------------------