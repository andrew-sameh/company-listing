from contextlib import asynccontextmanager
from collections import defaultdict
from fastapi import FastAPI
from core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from api.router import router as api_router
from service.companies_client import load_companies_data

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        app.state.data = await load_companies_data()
        app.state.score = defaultdict(int)
        yield
    finally:
        pass

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    lifespan=lifespan,
    docs_url="/",
)

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)