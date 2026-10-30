# Re-exporting models from vertical slices for backward compatibility and Alembic metadata
from sqlmodel import SQLModel

from app.auth.models import Message, NewPassword, Token, TokenPayload
from app.burgers.models import (
    Burger,
    BurgerBase,
    BurgerCreate,
    BurgerPublic,
    BurgersPublic,
    BurgerUpdate,
)
from app.items.models import (
    Item,
    ItemBase,
    ItemCreate,
    ItemPublic,
    ItemsPublic,
    ItemUpdate,
)
from app.users.models import (
    UpdatePassword,
    User,
    UserBase,
    UserCreate,
    UserPublic,
    UserRegister,
    UsersPublic,
    UserUpdate,
    UserUpdateMe,
    get_datetime_utc,
)

__all__ = [
    "SQLModel",
    "get_datetime_utc",
    "UserBase",
    "UserCreate",
    "UserRegister",
    "UserUpdate",
    "UserUpdateMe",
    "UpdatePassword",
    "User",
    "UserPublic",
    "UsersPublic",
    "ItemBase",
    "ItemCreate",
    "ItemUpdate",
    "Item",
    "ItemPublic",
    "ItemsPublic",
    "BurgerBase",
    "BurgerCreate",
    "BurgerUpdate",
    "Burger",
    "BurgerPublic",
    "BurgersPublic",
    "Message",
    "Token",
    "TokenPayload",
    "NewPassword",
]
