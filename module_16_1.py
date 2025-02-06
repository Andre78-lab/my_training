from fastapi import FastAPI
# Создаем экземпляр приложения FastAPI
app = FastAPI()

@app.get("/")
async def main_page():
    return "Главная страница!"

@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user_number(user_id):
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user")
async def user_info(username : str = "Andre", age: int = 45):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"