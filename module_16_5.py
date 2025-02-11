from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import Annotated, List


app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)

# Настраиваем Jinja2 для загрузки шаблонов из папки templates
templates = Jinja2Templates(directory="templates")

#users = {'1': 'Имя: Example, возраст: 18'}

class User(BaseModel):
    id: int
    username: str
    age: int

# Пустой список пользователей
users: List[User] = []

# Генерация ID для нового пользователя
def generate_id():
    if not users:
        return 1
    return users[-1].id + 1


@app.get("/", response_class=HTMLResponse)
async def get_tasks(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


# GET /users - Возвращает список всех пользователей
@app.get("/user/{user_id}", response_model=List[User])
async def get_users(request: Request, user_id: int):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "users": [user]})


@app.post("/user/{username}/{age}",response_model=User)
async def post_users(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")]
                     , age: Annotated[int, Path(ge=18, le=120, description="Enter age")]) -> str:
    new_user = User(id = generate_id(), username = username, age = age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}" , response_model=User)
async def put_users(user_id: int, username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")]
                     , age: Annotated[int, Path(ge=18, le=120, description="Enter age")]) -> str:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}", response_model=User)
async def delete_users(user_id: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")