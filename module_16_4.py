from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel,Field


# Создаем экземпляр приложения FastAPI
app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

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


# GET /users - Возвращает список всех пользователей
@app.get("/users", response_model=List[User])
async def get_users():
    return users



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