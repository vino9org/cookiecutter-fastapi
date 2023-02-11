from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    user_name: str
    comments: str


class UserRecord(UserBase, table=True):
    __tablename__ = "users"
    user_id: int = Field(default=None, primary_key=True)


class User(UserBase):
    pass
