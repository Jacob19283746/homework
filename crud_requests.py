from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Username: Example, Age: 18'}

@app.get('/users')
async def refund() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def add_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples={'example':'Jacob'})],
              age: Annotated[int, Path(ge=18, le=120, description='Enter age', examples={'example': 24})]) -> str:
    current_index = str(int(max(users.keys(), key=int)) + 1)
    users[current_index] = f'Username: {username}, Age: {age}'
    return f'User {current_index} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', examples={'example': 1})],
                 username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples={'example':'Jacob'})],
                 age: Annotated[int, Path(ge=18, le=120, description='Enter age', examples={'example': 24})]) -> str:
    user_id_str = str(user_id)
    users[user_id_str] = f'Username: {username}, Age: {age}'
    return f'User {user_id} has been updated'

@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', examples={'example': 1})]) -> str:
    user_id_str = str(user_id)
    del users[user_id_str]
    return f'User {user_id} has been deleted'


