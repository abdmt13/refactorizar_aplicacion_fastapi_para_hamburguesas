import uuid
from datetime import UTC, datetime

from sqlmodel import Field, SQLModel


def get_datetime_utc() -> datetime:
    return datetime.now(UTC)


# Propiedades compartidas
class BurgerBase(SQLModel):
    name: str = Field(min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=255)
    price: float = Field(gt=0)
    is_available: bool = Field(default=True)


# Propiedades para crear hamburguesa
class BurgerCreate(BurgerBase):
    pass


# Propiedades para actualizar hamburguesa
class BurgerUpdate(SQLModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=255)
    price: float | None = Field(default=None, gt=0)
    is_available: bool | None = None


# Tabla en Base de Datos
class Burger(BurgerBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime | None = Field(default_factory=get_datetime_utc)


# Propiedades para respuestas públicas
class BurgerPublic(BurgerBase):
    id: uuid.UUID
    created_at: datetime | None = None


class BurgersPublic(SQLModel):
    data: list[BurgerPublic]
    count: int
