import asyncpg
from homework.settings import DATABASE_URL


class Database():
    async def create_pool(self):

        self.pool = await asyncpg.create_pool(dsn=DATABASE_URL)
        print("Connection to PostgreSQL DB successful")
