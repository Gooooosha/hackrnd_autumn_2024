from redis.asyncio import Redis
from config import settings


class AsyncRedisClient:
    def __init__(self):
        self.url = settings.redis_storage
        self.redis = Redis.from_url(self.url)

    async def set_value(self, key: str, value: str, expire: int = None):
        await self.redis.set(key, value, ex=expire)

    async def get_value(self, key: str):
        value = await self.redis.get(key)
        return value.decode('utf-8')

    async def delete_value(self, key: str):
        await self.redis.delete(key)
