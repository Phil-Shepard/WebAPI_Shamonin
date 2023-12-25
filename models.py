from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    items = relationship('Item', back_populates='category')
    created_at = Column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='items')
    created_at = Column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    email = Column(String, index=True, unique=True)
    password = Column(String)
    created_at = Column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())
    # Добавьте дополнительные поля пользователя по необходимости
    # Например, имя, фамилия, роль и т.д.

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    item_id = Column(Integer, ForeignKey('items.id'))
    item = relationship('Item', back_populates='comments')
    created_at = Column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    items = relationship('Item', secondary='item_tags', back_populates='tags')

class ItemTag(Base):
    __tablename__ = 'item_tags'
    item_id = Column(Integer, ForeignKey('items.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id'), primary_key=True)
