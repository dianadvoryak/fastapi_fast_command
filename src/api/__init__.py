from fastapi import APIRouter

from src.api.books import db as db_router
from auth_login import auth_login


main_router = APIRouter()

main_router.include_router(db_router)
main_router.include_router(auth_login)
