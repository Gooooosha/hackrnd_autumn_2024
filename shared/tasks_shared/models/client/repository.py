from sqlalchemy import update, delete
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from typing import List, Optional

from tasks_shared.models.client.model import Client
from shared.schemas.client import (
    ClientUpdate,
    ClientCreate,
    Client as ClientSchema)


class ClientRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_contract_number_by_tg_id(self, tg_id: str) -> Optional[str]:
        result = await self.session.execute(
            select(Client).filter_by(tg_id=tg_id)
        )
        record = result.scalars().one_or_none()
        return record

    async def get_client_by_contract_number(self,
                                            contract_number: str
                                            ) -> Optional[ClientSchema]:
        result = await self.session.execute(
            select(Client).filter_by(contract_number=contract_number)
        )
        client = result.scalars().one_or_none()
        if client:
            return ClientSchema.model_validate(client).model_dump()

        return None

    async def add(self, model_create: ClientCreate) -> ClientSchema:
        new_record = Client(**model_create)
        self.session.add(new_record)

        await self.session.commit()
        await self.session.refresh(new_record)

        return ClientSchema.model_validate(new_record).model_dump()

    async def get_all(self) -> List[ClientSchema]:
        result = await self.session.execute(
            select(Client)
        )
        records = result.scalars().all()

        return [ClientSchema.model_validate(record).model_dump() for record in records]  # noqa: E501

    async def get_by_id(self, id: int) -> Optional[ClientSchema]:
        result = await self.session.execute(select(Client).filter_by(id=id))
        record = result.scalars().one_or_none()
        if record:
            return ClientSchema.model_validate(record).model_dump()

        return None

    async def update(self,
                     id: int,
                     model_update: ClientUpdate) -> Optional[ClientSchema]:
        await self.session.execute(
            update(Client).where(Client.id == id)
            .values(**model_update)
        )

        await self.session.commit()
        return await self.get_by_id(id=id)

    async def delete(self, id: int) -> bool:
        try:
            await self.session.execute(delete(Client).where(Client.id == id))
            await self.session.commit()
            return True
        except Exception:
            return False
