from shared.tasks_shared.database_utils import get_session
from shared.tasks_shared.models.intention.repository import IntentionRepository
from shared.schemas.intention import IntentionCreate, IntentionUpdate


async def add(model_create: IntentionCreate):
    async with get_session() as session:
        repo = IntentionRepository(session)
        return await repo.add(model_create=model_create)


async def get_by_id(id: int):
    async with get_session() as session:
        repo = IntentionRepository(session)
        return await repo.get_by_id(id=id)


async def update(id: int, model_update: IntentionUpdate):
    async with get_session() as session:
        repo = IntentionRepository(session)
        return await repo.update(id=id, model_update=model_update)


async def delete(id: int):
    async with get_session() as session:
        repo = IntentionRepository(session)
        return await repo.delete(id=id)


async def get_all():
    async with get_session() as session:
        repo = IntentionRepository(session)
        return await repo.get_all()
