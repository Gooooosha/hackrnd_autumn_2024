from sqlalchemy import update, delete
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from tasks_shared.models.reply.model import Reply
from shared.schemas.reply import (
    ReplyUpdate,
    ReplyCreate,
    Reply as ReplySchema)


class ReplyRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, create_model: ReplyCreate) -> ReplySchema:
        new_record = Reply(**create_model)
        self.session.add(new_record)

        await self.session.commit()
        await self.session.refresh(new_record)

        return ReplySchema.model_validate(new_record).model_dump()

    async def get_all(self) -> List[ReplySchema]:
        result = await self.session.execute(
            select(Reply)
        )
        clients = result.scalars().all()
        return [ReplySchema.model_validate(client).model_dump() for client in clients]  # noqa: E501

    async def get_by_id(self, id: int) -> Optional[ReplySchema]:
        result = await self.session.execute(select(Reply).filter_by(id=id))
        client = result.scalars().one_or_none()
        if client:
            return ReplySchema.model_validate(client).model_dump()

        return None

    async def update(self,
                     id: int,
                     update_model: ReplyUpdate) -> Optional[ReplySchema]:
        await self.session.execute(
            update(Reply).where(Reply.id == id)
            .values(**update_model)
        )

        await self.session.commit()
        return await self.get_by_id(id=id)

    async def delete(self, id: int) -> bool:
        try:
            await self.session.execute(delete(Reply).where(Reply.id == id))
            await self.session.commit()
            return True
        except Exception:
            return False
