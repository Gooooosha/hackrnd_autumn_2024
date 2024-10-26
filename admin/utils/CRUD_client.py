from shared.tasks_shared.database_utils import get_session
from shared.tasks_shared.models.client.repository import ClientRepository
from shared.schemas.client import ClientCreate, ClientUpdate, Client as ClientSchema


async def add(model_create: ClientCreate):
    async with get_session() as session:
        repo = ClientRepository(session)
        return await repo.add(model_create=model_create)


async def get_by_id(id: int):
    async with get_session() as session:
        repo = ClientRepository(session)
        return await repo.get_by_id(id=id)


async def update(id: int, model_update: ClientUpdate):
    async with get_session() as session:
        repo = ClientRepository(session)
        return await repo.update(id=id, model_update=model_update)


async def delete(id: int):
    async with get_session() as session:
        repo = ClientRepository(session)
        return await repo.delete(id=id)

async def get_all():
    async with get_session() as session:
        repo = ClientRepository(session)
        return await repo.get_all()
