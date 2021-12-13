import os
from database import Database
import asyncio
import numpy as np


def work_with_os():
    print(f'Имя ос - {os.name}')
    print(f'Имя пользователя - {os.getlogin()}')
    print(f'Список папок и директорий в папке - {os.listdir(path=".")}')


async def database_connect():

    db = Database
    await db.create_pool(db)


def work_with_numpy():
    a = np.random.sample((3, 3))
    print(a)
    print('-'*40)
    return a.transpose()


if __name__ == "__main__":
    work_with_os()
    print(work_with_numpy())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(database_connect())
