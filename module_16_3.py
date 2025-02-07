from fastapi import FastAPI, Path
from typing import Annotated
# Создаем экземпляр приложения FastAPI
app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def post_users(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")]
                     , age: Annotated[int, Path(ge=18, le=120, description="Enter age")]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'

@app.put("/user/{user_id}/{username}/{age}'")
async def put_users(user_id: int, username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")]
                     , age: Annotated[int, Path(ge=18, le=120, description="Enter age")]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def delete_users(user_id: str) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted."
