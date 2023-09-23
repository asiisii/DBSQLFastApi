from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True


# Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a
# dict, but an ORM model (or any other arbitrary object with attributes).

# This way, instead of only trying to get the id value from a dict, as in:
# id = data["id"]

# it will also try to get it from an attribute, as in:
# id = data.id
