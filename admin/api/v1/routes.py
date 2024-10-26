from fastapi import APIRouter
from .endpoints import (
    auth,
    reply,
    client,
    editor,
    purpose,
    intention
)


router = APIRouter(
    prefix="/api/v1",
)

router.include_router(auth.router)
router.include_router(reply.router)
router.include_router(client.router)
router.include_router(editor.router)
router.include_router(purpose.router)
router.include_router(intention.router)
