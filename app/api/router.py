from fastapi import APIRouter
from app.api.endpoints import email

router = APIRouter()

# Include endpoint routers
router.include_router(email.router, prefix="/generate_email", tags=["emails"])
