from sqlalchemy import update, delete
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from tasks_shared.models.editor.model import Editor
from shared.schemas.editor import (
    EditorUpdate,
    EditorCreate,
    Editor as EditorSchema)


class EditorRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def is_login_exist(self, login: str) -> bool:
        result = await self.session.execute(select(Editor).filter_by(login=login))
        record = result.scalars().one_or_none()
        return record is not None

    async def check_password(self, login: str, password: str) -> bool:
        result = await self.session.execute(
            select(Editor).filter_by(login=login,
                                     password=password)
        )
        record = result.scalars().one_or_none()
        if record:
            return EditorSchema.model_validate(record).model_dump()
        return None

    async def add(self, create_model: EditorCreate) -> EditorSchema:
        new_record = Editor(**create_model)
        self.session.add(new_record)

        await self.session.commit()
        await self.session.refresh(new_record)

        return EditorSchema.model_validate(new_record).model_dump()

    async def get_all(self) -> List[EditorSchema]:
        result = await self.session.execute(
            select(Editor)
        )
        records = result.scalars().all()
        return [EditorSchema.model_validate(record).model_dump() for record in records]  # noqa: E501

    async def get_by_id(self, id: int) -> Optional[EditorSchema]:
        result = await self.session.execute(select(Editor).filter_by(id=id))
        record = result.scalars().one_or_none()
        if record:
            return EditorSchema.model_validate(record).model_dump()

        return None

    async def update(self,
                     id: int,
                     update_model: EditorUpdate) -> Optional[EditorSchema]:
        await self.session.execute(
            update(Editor).where(Editor.id == id)
            .values(**update_model)
        )

        await self.session.commit()
        return await self.get_by_id(id=id)

    async def delete(self, id: int) -> bool:
        try:
            await self.session.execute(
                delete(Editor).where(Editor.id == id)
            )
            await self.session.commit()
            return True
        except Exception:
            return False
