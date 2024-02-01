from fastapi import FastAPI

from back.database import engine
from back.router import blog, user, login
from back import models
app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(login.router)
app.include_router(user.router)