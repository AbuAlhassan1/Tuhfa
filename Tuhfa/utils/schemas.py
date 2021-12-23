from ninja import Schema
import datetime

from pydantic import EmailStr, Field

class CategoryIn(Schema):
    name: str
    description: str
    image: str
    parent: int = None

class MessageOut(Schema):
    message: str

class ThemeIn(Schema):
    name: str
    title: str
    description: str
    image: str = None
    category: int
    date: datetime.datetime

class CategorySchema(Schema):
    name: str
    description: str
    image: str = None
    # parent: int = None

class CategoryOut(Schema):
    id: int
    name: str
    description: str
    image: str = None
    parent: CategorySchema = None

class ThemeOut(Schema):
    name: str
    title: str
    description: str
    image: str = None
    category: CategoryOut = None
    date: datetime.datetime

class ThemeSchema(Schema):
    name: str
    title: str
    description: str
    image: str = None
    category: CategoryOut
    date: datetime.datetime

class UserCreate(Schema):
    full_name: str
    email: str
    phone: int
    category: CategoryIn = None
    theme: ThemeSchema = None

class UserOut(Schema):
    full_name: str
    email: str
    phone: int
    category: CategoryIn = None
    theme: ThemeSchema = None

class PostSchema(Schema):
    title: str
    description: str
    image: str

class PostOut(Schema):
    title: str
    description: str
    image: str
    created_on: datetime.datetime
    updated_on: datetime.datetime

class AdminCreate(Schema):
    full_name: str
    email: EmailStr
    phone: int
    password1: str
    password2: str

class AdminOut(Schema):
    full_name: str = None
    email: EmailStr
    phone: str = None

class TokenOut(Schema):
    access: str

class AuthOut(Schema):
    token: TokenOut
    admin: AdminOut

class SignIn(Schema):
    email: EmailStr
    password: str

# class AdminUpdate(Schema):
#     full_name: str
#     email: EmailStr
#     phone: int

class UpdatePassword(Schema):
    old_password: str
    password1: str
    password2: str