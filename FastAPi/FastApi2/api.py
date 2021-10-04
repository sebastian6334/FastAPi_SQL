from fastapi.routing import APIRouter

from endpoints import items, customers, addresses

api_router = APIRouter()
api_router.include_router(customers.router,prefix="/customers", tags=["customers"])
api_router.include_router(items.router,prefix="/items", tags=["items"])
api_router.include_router(addresses.router,prefix="/addresses", tags=["addresses"])

