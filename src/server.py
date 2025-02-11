from fastapi import FastAPI
from src.routers import router


app = FastAPI(
    title="API - Predição de valores com Deep Learning (LSTM)",
    description=" O Objetivo do projeto é prever o valor das ações de uma empresa, utilizando dados históricos de preços. A biblioteca yFinance é usada para coletar informações financeiras, como o preço de fechamento diário das ações da Disney (DIS).",
    version="1.0.0"
)


app.include_router(router)