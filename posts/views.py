from typing import List
from django.shortcuts import render
from ninja import Router
from .models import Post
from Tuhfa.utils.schemas import PostSchema, MessageOut, PostOut

posts_controller = Router(tags=['posts'])


# ---------------------------------------------------------------

# Create A Post
@posts_controller.post('create_post', response={
    200: PostOut,
    400: MessageOut
})
def create_post(request, title, description, image):
    try:
        post = Post.objects.create(title=title, description=description, image=image)
    except:
        return 400, {'message': 'Error Creating Post'}
    return 200, post

# ---------------------------------------------------------------

# Get All Posts
@posts_controller.get('get_all_posts', response={
    200: List[PostOut],
    404: MessageOut
})
def get_all_posts(request):
    posts = Post.objects.all()
    return 200, posts

# ---------------------------------------------------------------

# Delete A Post
@posts_controller.delete('delete_post/{id}', response={
    200: MessageOut,
    404: MessageOut
})
def delete_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except:
        return 404, {'message': 'Post Not Found'}
    post.delete()
    return 200, {'message': 'Post Deleted'}

# ---------------------------------------------------------------
