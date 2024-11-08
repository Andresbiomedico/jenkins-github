import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.utilities.enviroment import EnvironmentSettings

env = EnvironmentSettings()

app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
)
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "server on line"}


if __name__ == "__main__":
    uvicorn.run(app)

