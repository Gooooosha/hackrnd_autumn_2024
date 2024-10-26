from sqlalchemy import update, delete
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from typing import List, Optional

from tasks_shared.models.purpose.model import Purpose
from shared.schemas.purpose import (
    PurposeUpdate,
    PurposeCreate,
    Purpose as PurposeSchema)


class PurposeRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, create_model: PurposeCreate) -> PurposeSchema:
        new_record = Purpose(**create_model)
        self.session.add(new_record)

        await self.session.commit()
        await self.session.refresh(new_record)

        return PurposeSchema.model_validate(new_record).model_dump()

    async def get_all(self) -> List[PurposeSchema]:
        result = await self.session.execute(
            select(Purpose)
        )
        records = result.scalars().all()

        return [PurposeSchema.model_validate(record).model_dump() for record in records]

    async def get_by_id(self, id: int) -> Optional[PurposeSchema]:
        result = await self.session.execute(select(Purpose).filter_by(id=id))
        record = result.scalars().one_or_none()
        if record:
            return PurposeSchema.model_validate(record).model_dump()

        return None

    async def update(self, id: int, update_model: PurposeUpdate) -> Optional[PurposeSchema]:
        await self.session.execute(
            update(Purpose).where(Purpose.id == id)
            .values(**update_model)
        )

        await self.session.commit()
        return await self.get_by_id(id=id)

    async def delete(self, id: int) -> bool:
        try:
            await self.session.execute(delete(Purpose).where(Purpose.id == id))
            await self.session.commit()
            return True
        except Exception as e:
            return False
