from shared.tasks_shared.database_utils import get_session
from shared.tasks_shared.models.mail.repository import MailRepository
from shared.schemas.mail import MailCreate, MailUpdate


async def add(model_create: MailCreate):
    async with get_session() as session:
        repo = MailRepository(session)
        return await repo.add(model_create=model_create)


async def get_by_id(id: int):
    async with get_session() as session:
        repo = MailRepository(session)
        return await repo.get_by_id(id=id)


async def update(id: int, model_update: MailUpdate):
    async with get_session() as session:
        repo = MailRepository(session)
        return await repo.update(id=id, model_update=model_update)


async def delete(id: int):
    async with get_session() as session:
        repo = MailRepository(session)
        return await repo.delete(id=id)

async def get_all():
    async with get_session() as session:
        repo = MailRepository(session)
        return await repo.get_all()
