from typing import List, Optional

from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect

import schemas
from database import get_db
from sqlalchemy.orm import Session
from crud import (
    create_user, get_users, get_user, update_user, delete_user,
    create_comment, get_comments, get_comment, update_comment, delete_comment,
    create_tag, get_tags, get_tag, update_tag, delete_tag
)

router_websocket = APIRouter()
router_users = APIRouter(prefix='/users', tags=['user'])
router_comments = APIRouter(prefix='/comments', tags=['comment'])
router_tags = APIRouter(prefix='/tags', tags=['tag'])


# WebSocket
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


async def notify_clients(message: str):
    for connection in manager.active_connections:
        await connection.send_text(message)


@router_websocket.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    await manager.broadcast(f"Client #{client_id} joined the chat")
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")


# Users
@router_users.post("/", response_model=schemas.User)
async def create_user_route(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, user_data)
    await notify_clients(f"User added: {user.username}")
    return user


@router_users.get("/", response_model=List[schemas.User])
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router_users.get("/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    return user


@router_users.patch("/{user_id}", response_model=schemas.User)
async def update_user_route(user_id: int, user_data: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user_data)
    if updated_user:
        await notify_clients(f"User updated: {updated_user.username}")
        return updated_user
    return {"message": "User not found"}


@router_users.delete("/{user_id}")
async def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    deleted = delete_user(db, user_id)
    if deleted:
        await notify_clients(f"User deleted: ID {user_id}")
        return {"message": "User deleted"}
    return {"message": "User not found"}


# Comments
@router_comments.post("/", response_model=schemas.Comment)
async def create_comment_route(comment_data: schemas.CommentCreate, db: Session = Depends(get_db)):
    comment = create_comment(db, comment_data)
    await notify_clients(f"Comment added: {comment.text}")
    return comment


@router_comments.get("/", response_model=List[schemas.Comment])
async def read_comments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    comments = get_comments(db, skip=skip, limit=limit)
    return comments


@router_comments.get("/{comment_id}", response_model=schemas.Comment)
async def read_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = get_comment(db, comment_id)
    return comment


@router_comments.patch("/{comment_id}", response_model=schemas.Comment)
async def update_comment_route(comment_id: int, comment_data: schemas.CommentUpdate, db: Session = Depends(get_db)):
    updated_comment = update_comment(db, comment_id, comment_data)
    if updated_comment:
        await notify_clients(f"Comment updated: {updated_comment.text}")
        return updated_comment
    return {"message": "Comment not found"}


@router_comments.delete("/{comment_id}")
async def delete_comment_route(comment_id: int, db: Session = Depends(get_db)):
    deleted = delete_comment(db, comment_id)
    if deleted:
        await notify_clients(f"Comment deleted: ID {comment_id}")
        return {"message": "Comment deleted"}
    return {"message": "Comment not found"}


# Tags
@router_tags.post("/", response_model=schemas.Tag)
async def create_tag_route(tag_data: schemas.TagCreate, db: Session = Depends(get_db)):
    tag = create_tag(db, tag_data)
    await notify_clients(f"Tag added: {tag.name}")
    return tag


@router_tags.get("/", response_model=List[schemas.Tag])
async def read_tags(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tags = get_tags(db, skip=skip, limit=limit)
    return tags


@router_tags.get("/{tag_id}", response_model=schemas.Tag)
async def read_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = get_tag(db, tag_id)
    return tag


@router_tags.patch("/{tag_id}", response_model=schemas.Tag)
async def update_tag_route(tag_id: int, tag_data: schemas.TagUpdate, db: Session = Depends(get_db)):
    updated_tag = update_tag(db, tag_id, tag_data)
    if updated_tag:
        await notify_clients(f"Tag updated: {updated_tag.name}")
        return updated_tag
    return {"message": "Tag not found"}


@router_tags.delete("/{tag_id}")
async def delete_tag_route(tag_id: int, db: Session = Depends(get_db)):
    deleted = delete_tag(db, tag_id)
    if deleted:
        await notify_clients(f"Tag deleted: ID {tag_id}")
        return {"message": "Tag deleted"}
    return {"message": "Tag not found"}
