from ninja import Schema
import datetime

class CategoryIn(Schema):
    name: str
    description: str
    parent: int = None


class MessageOut(Schema):
    message: str

class UserCreate(Schema):
    full_name: str
    email: str
    phone: int
    category: int
    theme: int



class ThemeIn(Schema):
    name: str
    title: str
    description: str
    category: int
    date: datetime.datetime

class CategorySchema(Schema):
    name: str
    description: str
    parent: int = None

class CategoryOut(Schema):
    name: str
    description: str
    parent: CategorySchema = None

class ThemeOut(Schema):
    name: str
    title: str
    description: str
    category: CategoryOut = None
    date: datetime.datetime

class ThemeSchema(Schema):
    name: str
    title: str
    description: str
    category: CategoryOut
    date: datetime.datetime


class UserOut(Schema):
    full_name: str
    email: str
    phone: int
    category: CategorySchema
    theme: ThemeSchema

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
