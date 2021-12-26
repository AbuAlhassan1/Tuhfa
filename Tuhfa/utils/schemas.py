from ninja import Schema, schema
import datetime
from ninja.files import UploadedFile

from pydantic import EmailStr, Field

class MessageOut(Schema):
    message: str

# ---------------------------------------------------------------

# Category Schemas
class CategoryIn(Schema):
    name: str
    description: str
    parent: int = None


# class CategorySchema(Schema):
#     name: str
#     description: str
#     image: str = None
#     # parent: int = None

class CategoryOut(Schema):
    id: int
    name: str
    description: str
    image: str = None
    parent: int
# ---------------------------------------------------------------

# Theme Schemas
class ThemeCategorySchema(Schema):
    id: int
    name: str

class ThemeIn(Schema):
    name: str
    title: str
    description: str
    image: str = None
    date: datetime.datetime
    category: int

class ThemeOut(Schema):
    name: str
    title: str
    description: str
    image: str = None
    date: datetime.datetime
    category: ThemeCategorySchema = None

class ThemeSchema(Schema):
    name: str
    title: str
    description: str
    image: str = None
    category: CategoryOut
    date: datetime.datetime

# ---------------------------------------------------------------
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

class UpdatePassword(Schema):
    old_password: str
    password1: str
    password2: str

# ---------------------------------------------------------------

# About Schemas
class AboutOut(Schema):
    image: str
    description: str
    created: datetime.date
    updated: datetime.date

# ---------------------------------------------------------------

# Schedule Schemas
class ScheduleOut(Schema):
    id: int
    Sunday: str
    Monday: str
    Tuesday: str
    Wednesday: str
    Thursday: str
    Friday: str
    Saturday: str
    created: datetime.date
    updated: datetime.datetime

class ScheduleIn(Schema):
    Sunday: str
    Monday: str
    Tuesday: str
    Wednesday: str
    Thursday: str
    Friday: str
    Saturday: str

# ---------------------------------------------------------------