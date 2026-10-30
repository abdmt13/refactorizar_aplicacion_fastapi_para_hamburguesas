import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from app.auth.deps import get_current_active_superuser
from app.auth.models import Message
from app.burgers import service as burger_service
from app.burgers.models import (
    BurgerCreate,
    BurgerPublic,
    BurgersPublic,
    BurgerUpdate,
)
from app.core.db import SessionDep

router = APIRouter(prefix="/burgers", tags=["burgers"])


@router.get("/", response_model=BurgersPublic)
def read_burgers(
    session: SessionDep, skip: int = 0, limit: int = 100
) -> Any:
    """
    Listar hamburguesas disponibles.
    """
    burgers, count = burger_service.get_burgers(session, skip=skip, limit=limit)
    items_public = [BurgerPublic.model_validate(b) for b in burgers]
    return BurgersPublic(data=items_public, count=count)


@router.get("/{id}", response_model=BurgerPublic)
def read_burger(session: SessionDep, id: uuid.UUID) -> Any:
    """
    Obtener una hamburguesa por ID.
    """
    burger = burger_service.get_burger_by_id(session, id)
    if not burger:
        raise HTTPException(status_code=404, detail="Hamburguesa no encontrada")
    return burger


@router.post(
    "/",
    dependencies=[Depends(get_current_active_superuser)],
    response_model=BurgerPublic,
)
def create_burger(
    *, session: SessionDep, burger_in: BurgerCreate
) -> Any:
    """
    Crear nueva hamburguesa (solo superusuarios/admin).
    """
    return burger_service.create_burger(session=session, burger_in=burger_in)


@router.put(
    "/{id}",
    dependencies=[Depends(get_current_active_superuser)],
    response_model=BurgerPublic,
)
def update_burger(
    *,
    session: SessionDep,
    id: uuid.UUID,
    burger_in: BurgerUpdate,
) -> Any:
    """
    Actualizar datos de una hamburguesa.
    """
    burger = burger_service.get_burger_by_id(session, id)
    if not burger:
        raise HTTPException(status_code=404, detail="Hamburguesa no encontrada")
    return burger_service.update_burger(session=session, db_burger=burger, burger_in=burger_in)


@router.delete(
    "/{id}",
    dependencies=[Depends(get_current_active_superuser)],
    response_model=Message,
)
def delete_burger(
    session: SessionDep, id: uuid.UUID
) -> Message:
    """
    Eliminar una hamburguesa.
    """
    burger = burger_service.get_burger_by_id(session, id)
    if not burger:
        raise HTTPException(status_code=404, detail="Hamburguesa no encontrada")
    burger_service.delete_burger(session=session, db_burger=burger)
    return Message(message="Hamburguesa eliminada correctamente")
