from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    age: int

data = UserIn(username='robert.dh.keum', age=44)
print('username', data.username)
print('age', data.age, type(data.age))

print('as dict:', data.model_dump())