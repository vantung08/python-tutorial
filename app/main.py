# from greeting import greeting

# def main():
#     return greeting()

# if __name__ == '__main__':
#     print(main())

import logging
from fastapi import FastAPI
from app.routers import greeting


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

app.include_router(greeting.router)

@app.get("/")
async def root():
    return {"message": "Hello Application"}