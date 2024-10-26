from sqlalchemy import update, delete
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from tasks_shared.models.mail.model import Mail
from shared.schemas.mail import (
    MailUpdate,
    MailCreate,
    Mail as MailSchema)


class MailRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, create_model: MailCreate) -> MailSchema:
        new_record = Mail(**create_model)
        self.session.add(new_record)

        await self.session.commit()
        await self.session.refresh(new_record)

        return MailSchema.model_validate(new_record).model_dump()

    async def get_all(self) -> List[MailSchema]:
        result = await self.session.execute(
            select(Mail)
        )
        records = result.scalars().all()

        return [MailSchema.model_validate(record).model_dump() for record in records]  # noqa

    async def get_by_id(self, id: int) -> Optional[MailSchema]:
        result = await self.session.execute(select(Mail).filter_by(id=id))
        record = result.scalars().one_or_none()
        if record:
            return MailSchema.model_validate(record).model_dump()

        return None

    async def update(self,
                     id: int,
                     update_model: MailUpdate) -> Optional[MailSchema]:
        await self.session.execute(
            update(Mail).where(Mail.id == id)
            .values(**update_model)
        )

        await self.session.commit()
        return await self.get_by_id(id=id)

    async def delete(self, id: int) -> bool:
        try:
            await self.session.execute(delete(Mail).where(Mail.id == id))
            await self.session.commit()
            return True
        except Exception as e:
            return False
