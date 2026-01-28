from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str


    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TaskCreate(BaseModel):
    title: str
    description: str


class TaskUpdate(BaseModel):
    title: str = None
    description: str = None
    status: str = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str

    class Config:
        from_attributes = True