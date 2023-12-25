from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import datetime


# Category
class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    name: Optional[str] = None


class Category(CategoryBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime


# Item
class ItemBase(BaseModel):
    name: str
    category_id: int


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    name: Optional[str] = None
    category_id: Optional[int] = None


class Item(ItemBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime

# User
class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime


# Comment
class CommentBase(BaseModel):
    text: str
    user_id: int
    item_id: int


class CommentCreate(CommentBase):
    pass


class CommentUpdate(CommentBase):
    text: Optional[str] = None
    user_id: Optional[int] = None
    item_id: Optional[int] = None


class Comment(CommentBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime


# Tag
class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    pass


class TagUpdate(TagBase):
    name: Optional[str] = None


class Tag(TagBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
