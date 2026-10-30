from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine, select

from app.core.config import settings

engine = create_engine(str(settings.DATABASE_URL), pool_pre_ping=True)


def get_db() -> Generator[Session]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]


def init_db(session: Session) -> None:
    # Tables can be created manually (e.g. in HeidiSQL) or with SQLModel.metadata.create_all(engine)
    # from sqlmodel import SQLModel
    # SQLModel.metadata.create_all(engine)

    from app.users import service as user_service
    from app.users.models import User, UserCreate

    user = session.exec(
        select(User).where(User.email == settings.FIRST_SUPERUSER)
    ).first()
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = user_service.create_user(session=session, user_create=user_in)

