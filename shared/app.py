import asyncio

from tasks_shared import database
from tasks_shared.database_utils import cook_models

from shared.utils.logger import Logger

asyncio.run(cook_models())
asyncio.run(database.init_db())


logger = Logger('common')
