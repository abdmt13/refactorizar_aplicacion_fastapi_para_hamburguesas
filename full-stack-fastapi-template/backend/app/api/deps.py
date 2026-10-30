# Re-exporting dependencies from core and auth for backward compatibility
from app.auth.deps import (
    CurrentUser,
    TokenDep,
    get_current_active_superuser,
    get_current_user,
    reusable_oauth2,
)
from app.core.db import SessionDep, get_db

__all__ = [
    "get_db",
    "SessionDep",
    "reusable_oauth2",
    "TokenDep",
    "get_current_user",
    "CurrentUser",
    "get_current_active_superuser",
]
