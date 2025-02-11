from fastapi import APIRouter
from api.endpoints import company


router = APIRouter()
router.include_router(company.router , tags=["Company"])