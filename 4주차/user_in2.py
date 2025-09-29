from pydantic import BaseModel, ValidationError
from typing import Optional

class UserIn2(BaseModel):
    username: str
    age: Optional[int] = None

u1 = UserIn2(username='dagam')
print('u1', u1)
print('u1.model_dump()', u1.model_dump())

u2 = UserIn2(username='dajin', age=2)
print('u2', u2)
print('u2.model_dump()', u2.model_dump())

u3 = UserIn2(username='jun', age="42")
print('u3', u3)
print('u3.model_dump()', u3.model_dump())

try:
    u_err = UserIn2(username='jin', age="test")
    print('u_err', u_err)
    print('u_err.model_dump()', u_err.model_dump())
except ValidationError as e:
    print('ValidationError !')
    print(e)
    print('e.erros()', e.erros())
