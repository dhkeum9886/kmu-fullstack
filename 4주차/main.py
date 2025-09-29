from datetime import datetime
from typing import Annotated
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field, EmailStr, ConfigDict

app = FastAPI()


class Address(BaseModel):
    city: str
    zip_code: str = Field(pattern=r"^\d{5}$")


class UserIn(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    age: int = Field(ge=0, le=120)
    email: EmailStr
    password: str = Field(min_length=8)
    address: Address | None = None


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    joined_at: datetime
    model_config = ConfigDict(from_attributes=True)

@app.get("/")
def index_page():
    return {'message': '풀스택서비스 구축실습중'}


@app.post("/users", response_model=UserOut, status_code=201)
def create_user(user: UserIn):
    return UserOut(
        id=1,
        username=user.username,
        email=user.email,
        joined_at=datetime.utcnow()
    )


@app.get("/users/{user_id}", response_model=UserOut)
def get_user(
        user_id: Annotated[int, Path(gt=0)],
        limit: Annotated[int, Query(ge=1, le=100)] = 10
):
    return UserOut(
        id=user_id,
        username="dhkeum9886",
        email="dhkeum9886@kookmin.ac.kr",
        joined_at=datetime.utcnow()
    )
