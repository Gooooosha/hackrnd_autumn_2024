from shared.tasks_shared.database_utils import get_session
from shared.tasks_shared.models.editor.repository import EditorRepository
from shared.utils.hash import hash_password
from typing import Optional, Dict
from shared.utils.jwt_manager import create_access_token, decode_access_token


class AuthService:
    @staticmethod
    async def login(login: str, password: str) -> Optional[Dict[str, str]]:
        async with get_session() as session:
            repo = EditorRepository(session)
            exist = await repo.is_login_exist(login=login)
            if exist:
                return await repo.check_password(login=login,
                                                 password=hash_password(password))  # noqa
            else:
                return {'error': 'Такого пользователя не существует'}

    @staticmethod
    async def get_token(role: str) -> str:
        return create_access_token(data={'role': role})

    @staticmethod
    async def get_role(token: str) -> str:
        return decode_access_token(token=token, key='role')
