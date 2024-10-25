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

    async def get_contract_numbers_by_tg_id(self, tg_id: str) -> Optional[str]:
        result = await self.session.execute(
            select(Client).filter(Client.tg_id == tg_id)
        )
        contract_number = result.scalar_one_or_none()
        return contract_number

    
    async def get_client_by_contract_number(self, contract_number: str) -> Optional[ClientSchema]:
        result = await self.session.execute(select(Client).filter_by(contract_number=contract_number))
        client = result.scalars().one_or_none()
        if client:
            return ClientSchema.model_validate(client).model_dump()

        return None

    async def add_client(self, client_create: ClientCreate) -> ClientSchema:
        new_client = Client(**client_create)
        self.session.add(new_client)

        await self.session.commit()
        await self.session.refresh(new_client)

        return ClientSchema.model_validate(new_client).model_dump()

    async def get_all(self) -> List[ClientSchema]:
        result = await self.session.execute(
            select(Client)
        )
        clients = result.scalars().all()

        return [ClientSchema.model_validate(client).model_dump() for client in clients]

    async def get_client_by_id(self, client_id: int) -> Optional[ClientSchema]:
        result = await self.session.execute(select(Client).filter_by(id=client_id))
        client = result.scalars().one_or_none()
        if client:
            return ClientSchema.model_validate(client).model_dump()

        return None

    async def update_client(self, client_id: int, client_update: ClientUpdate) -> Optional[ClientSchema]:
        await self.session.execute(
            update(Client).where(Client.id == client_id)
            .values(**client_update)
        )

        await self.session.commit()
        return await self.get_client_by_id(client_id)

    async def delete_client(self, client_id: int) -> bool:
        try:
            await self.session.execute(delete(Client).where(Client.id == client_id))
            await self.session.commit()
            return True
        except Exception as e:
            return False