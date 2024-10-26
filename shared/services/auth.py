from utils.redis import AsyncRedisClient
from config import Settings

class AuthService:
    def __init__(self):
        self.redis = AsyncRedisClient()

    async def add_token(self, tg_id: str, token: str):
        return await self.redis.set_value(key=tg_id,
                                          value= token,
                                          expire=Settings.token_expire)

    async def token_is_exist(self, tg_id: str):
        return await self.redis.get_value(tg_id)
    
    async def verify_token(self, tg_id: str, token: str):
        if await self.token_is_exist(tg_id):
            return await self.redis.get_value(key=tg_id) == token
        return {'error': 'Истекло время действия токена'}
