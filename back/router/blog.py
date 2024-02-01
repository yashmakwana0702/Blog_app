from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, auth
from sqlalchemy.orm import Session
from ..ORM import blog

get_db = database.get_db

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)


# GET ALL BLOG DATA
@router.get("/", response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    return blog.get_all(db)


# CREATE BLOG
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db),
           current_user: schemas.User = Depends(auth.get_current_user)):
    return blog.create(request, db)


# GET BLOG DATA BASED ON ID
@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    return blog.show(id, db)


# DELETE BLOG
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    return blog.delete(id, db)


# UPDATE BLOG
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def updated(id: int, request: schemas.Blog, db: Session = Depends(get_db),
            current_user: schemas.User = Depends(auth.get_current_user)):
    return blog.update(id, request, db)