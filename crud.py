import schemas
from models import User, Comment, Item, Tag, Category

from sqlalchemy.orm import Session


# User
def create_user(db: Session, schema: schemas.UserCreate):
    db_user = User(**schema.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter_by(id=user_id).first()


def update_user(db: Session, user_id: int, user_data: schemas.UserUpdate | dict):
    db_user = db.query(User).filter_by(id=user_id).first()

    user_data = user_data if isinstance(user_data, dict) else user_data.model_dump()

    if db_user:
        for key, value in user_data.items():
            if hasattr(db_user, key):
                setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)
        return db_user
    return None


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter_by(id=user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False


# Comment
def create_comment(db: Session, schema: schemas.CommentCreate):
    db_comment = Comment(**schema.model_dump())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_comments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Comment).offset(skip).limit(limit).all()


def get_comment(db: Session, comment_id: int):
    return db.query(Comment).filter_by(id=comment_id).first()


def update_comment(db: Session, comment_id: int, comment_data: schemas.CommentUpdate | dict):
    db_comment = db.query(Comment).filter_by(id=comment_id).first()

    comment_data = comment_data if isinstance(comment_data, dict) else comment_data.model_dump()

    if db_comment:
        for key, value in comment_data.items():
            if hasattr(db_comment, key):
                setattr(db_comment, key, value)

        db.commit()
        db.refresh(db_comment)
        return db_comment
    return None


def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(Comment).filter_by(id=comment_id).first()
    if db_comment:
        db.delete(db_comment)
        db.commit()
        return True
    return False


# Tag
def create_tag(db: Session, schema: schemas.TagCreate):
    db_tag = Tag(**schema.model_dump())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def get_tags(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Tag).offset(skip).limit(limit).all()


def get_tag(db: Session, tag_id: int):
    return db.query(Tag).filter_by(id=tag_id).first()


def update_tag(db: Session, tag_id: int, tag_data: schemas.TagUpdate | dict):
    db_tag = db.query(Tag).filter_by(id=tag_id).first()

    tag_data = tag_data if isinstance(tag_data, dict) else tag_data.model_dump()

    if db_tag:
        for key, value in tag_data.items():
            if hasattr(db_tag, key):
                setattr(db_tag, key, value)

        db.commit()
        db.refresh(db_tag)
        return db_tag
    return None


def delete_tag(db: Session, tag_id: int):
    db_tag = db.query(Tag).filter_by(id=tag_id).first()
    if db_tag:
        db.delete(db_tag)
        db.commit()
        return True
    return False


# Category
def create_category(db: Session, schema: schemas.CategoryCreate):
    db_category = Category(**schema.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Category).offset(skip).limit(limit).all()


def get_category(db: Session, category_id: int):
    return db.query(Category).filter_by(id=category_id).first()


def update_category(db: Session, category_id: int, category_data: schemas.CategoryUpdate | dict):
    db_category = db.query(Category).filter_by(id=category_id).first()

    category_data = category_data if isinstance(category_data, dict) else category_data.model_dump()

    if db_category:
        for key, value in category_data.items():
            if hasattr(db_category, key):
                setattr(db_category, key, value)

        db.commit()
        db.refresh(db_category)

    return db_category


def delete_category(db: Session, category_id: int):
    db_category = db.query(Category).filter_by(id=category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
        return True
    return False


# Item
def create_item(db: Session, schema: schemas.ItemCreate):
    db_item = Item(**schema.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int):
    return db.query(Item).filter_by(id=item_id).first()


def update_item(db: Session, item_id: int, item_data: schemas.ItemUpdate | dict):
    db_item = db.query(Item).filter_by(id=item_id).first()

    item_data = item_data if isinstance(item_data, dict) else item_data.model_dump()

    if db_item:
        for key, value in item_data.items():
            if hasattr(db_item, key):
                setattr(db_item, key, value)

        db.commit()
        db.refresh(db_item)
        return db_item
    return None


def delete_item(db: Session, item_id: int):
    db_item = db.query(Item).filter_by(id=item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    return False
