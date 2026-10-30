import uuid

from sqlmodel import Session, col, func, select

from app.burgers.models import Burger, BurgerCreate, BurgerUpdate


def get_burgers(
    session: Session, skip: int = 0, limit: int = 100
) -> tuple[list[Burger], int]:
    count_statement = select(func.count()).select_from(Burger)
    count = session.exec(count_statement).one()
    statement = (
        select(Burger).order_by(col(Burger.created_at).desc()).offset(skip).limit(limit)
    )
    burgers = list(session.exec(statement).all())
    return burgers, count


def get_burger_by_id(session: Session, burger_id: uuid.UUID) -> Burger | None:
    return session.get(Burger, burger_id)


def create_burger(session: Session, burger_in: BurgerCreate) -> Burger:
    db_burger = Burger.model_validate(burger_in)
    session.add(db_burger)
    session.commit()
    session.refresh(db_burger)
    return db_burger


def update_burger(
    session: Session, db_burger: Burger, burger_in: BurgerUpdate
) -> Burger:
    update_data = burger_in.model_dump(exclude_unset=True)
    db_burger.sqlmodel_update(update_data)
    session.add(db_burger)
    session.commit()
    session.refresh(db_burger)
    return db_burger


def delete_burger(session: Session, db_burger: Burger) -> None:
    session.delete(db_burger)
    session.commit()
