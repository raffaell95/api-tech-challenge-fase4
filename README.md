# APi Tech Challenge Fase 4 - FIAP

## Configuração da api


### Rodar a API usando Docker
- Para subir a api local usando doccker basta seguir os seguintes passos:
 1 - Entrar na pasta raiz da aplicação
 2 - rodar o comando `docker compose up -d` a aplicação estara rodando na porta `http://localhost:8000/docs` 
 
### Rodar a API sem Docker
 OPICIONAL: para rodar a aplicação localmente sem docker 
 1 - basta criar um ambiente virtual usando o comando `python3 -m venv venv`
 2 - em seguinda rodar o comando no linux `source venv/bin/activate` no windows `./venv/Scripts/activate`
 3 - baixar as dependencias necessarias usando `pip install -r requirements.txt`
 4 - para rodar a API basta rodar `fastapi run src/server.py` com ambiente virtual ativado.


# Usabilidade

- Para realizar previsões de valores é so acessar o endpoint `http://localhost:8000/api/v1/predict` do tipo `POST`, passando os paramentros `simbol, start_date, end_date`, para realizar testes de conversão basta acessar `http://localhost:8000/docs`.

 - simbol: é a nomeclatura da ação que se deseja realizar a previsão dos dados, como por exemplo:

    AAPL - Apple Inc.
    MSFT - Microsoft Corporation
    GOOGL - Alphabet Inc. (Google)
    AMZN - Amazon.com, Inc.
    TSLA - Tesla, Inc.
    NFLX - Netflix, Inc.
    META - Meta Platforms, Inc. (Facebook)
    DIS - The Walt Disney Company

- start_date: Se refere a data inicial para realização das previções
- end_date: Se refere a data final para realização das previções
