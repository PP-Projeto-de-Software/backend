from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.models import cliente_models, veiculo_models, ordem_servico_models

from app.routes import (
    cliente_routes,
    veiculo_routes,
    ordem_servico_routes
)

Base.metadata.create_all(bind=engine)



app = FastAPI(
    title="Souza Car API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():

    return {
        "message": "API Souza Car funcionando"
    }

app.include_router(cliente_routes.router)
app.include_router(veiculo_routes.router)
app.include_router(ordem_servico_routes.router)
