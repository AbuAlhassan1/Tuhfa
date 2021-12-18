from jose import jwt, JWTError
from ninja.security import HttpBearer
from django.conf import settings

class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            user_pk = jwt.decode(token=token, key=settings.SECRET_KEY, algorithms=['HS256'])
        except JWTError:
            return {
                'token': 'unauthorized',
            }
        
        if user_pk:
            return {
                'pk': str(user_pk['pk'])
            }

def get_user_token(user):
    token = jwt.encode({'pk': str(user.pk)}, key=settings.SECRET_KEY, algorithm='HS256')
    return {
        'access': str(token),
    }