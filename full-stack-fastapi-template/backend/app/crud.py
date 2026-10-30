# Re-exporting CRUD functions from vertical slices for backward compatibility
from app.auth.service import authenticate
from app.items.service import create_item
from app.users.service import create_user, get_user_by_email, update_user

__all__ = [
    "create_user",
    "update_user",
    "get_user_by_email",
    "authenticate",
    "create_item",
]
