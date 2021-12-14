from fastapi import FastAPI, HTTPException, status
import re

import uvicorn


app = FastAPI()


@app.post('/registration')
async def registr(request: str):
    """
    Функция проверяет пароль,
        подходит он по условиям или нет, возврашает jwt-token
    Условия:
    ◦ Должен быть не менее 6 символов;
    ◦ Должен содержать хотя бы одну цифру;
    ◦ Не должен состоять только из цифр;
    ◦ Не должен содержать слово “password” в любом регистре.
    """
    if len(request) < 6 or request.isdigit() or not bool(re.search(r'\d', request)) or request.lower == 'password':

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Bad password, password shoud be better :)")

    # generate a jwt token and return

    return {"access_token": "True", "token_type": "bearer"}


@app.get('/fibonachi')
def fib(n: int):
    """Функция возвращает заданное число Фибоначи"""
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8081, reload=True)
