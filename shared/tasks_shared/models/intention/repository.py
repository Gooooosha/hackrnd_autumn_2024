from sqlalchemy import update, delete
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from tasks_shared.models.intention.model import Intention
from shared.schemas.intention import (
    IntentionUpdate,
    IntentionCreate,
    Intention as IntentionSchema,
    IntentionFull)


class IntentionRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, create_model: IntentionCreate) -> IntentionSchema:
        new_record = Intention(**create_model)
        self.session.add(new_record)

        await self.session.commit()
        await self.session.refresh(new_record)

        return IntentionSchema.model_validate(new_record).model_dump()

    async def get_all(self) -> List[IntentionSchema]:
        result = await self.session.execute(
            select(Intention)
        )
        records = result.scalars().all()

        return [IntentionSchema.model_validate(record).model_dump() for record in records]

    async def get_all_joined(self) -> List[IntentionFull]:
        result = await self.session.execute(
            select(Intention).join(Intention.purpose_id).join(Intention.reply_id).join(Intention.mail_id)  # noqa
        )
        records = result.scalars().all()

        return [IntentionFull.model_validate(record).model_dump() for record in records]

    async def get_by_id(self, id: int) -> Optional[IntentionSchema]:
        result = await self.session.execute(select(Intention).filter_by(id=id))
        client = result.scalars().one_or_none()
        if client:
            return IntentionSchema.model_validate(client).model_dump()

        return None

    async def update(self,
                     id: int,
                     update_model: IntentionUpdate) -> Optional[IntentionSchema]:
        await self.session.execute(
            update(Intention).where(Intention.id == id)
            .values(**update_model)
        )

        await self.session.commit()
        return await self.get_by_id(id=id)

    async def delete(self, id: int) -> bool:
        try:
            await self.session.execute(delete(Intention).where(Intention.id == id))
            await self.session.commit()
            return True
        except Exception as e:
            return False
