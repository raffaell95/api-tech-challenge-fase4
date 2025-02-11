from fastapi import APIRouter, status
from fastapi import status, APIRouter
import tensorflow as tf
import yfinance as yf
import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler
from api.src.schemas.schemas import FinancyDataSchema

router = APIRouter()


@router.post('/api/v1/predict',
             summary="Realizar predição de valores",
             description="""Realizar predição de valores, usando como base biblioteca yFinance \n
             exemplo: {
                     "symbol": "DIS",
                     "start_date": "2023-02-11",
                     "end_date": "2025-02-11"
                    }""",
             status_code=status.HTTP_201_CREATED)
def predict(data: FinancyDataSchema):

    try:
        # Baixar dados financeiros
 
        df = yf.download(data.symbol, start=data.start_date, end=data.end_date)

        # Buscando o Caminho do arquivo
        model_path = os.path.join(os.getcwd(), "api", "LSTMTrained", "LSTM-TrainedModel.h5")
        
        # Carregar o modelo treinado
        model = tf.keras.models.load_model(model_path)

        # Selecionar a coluna que você quer prever, por exemplo, "Close"
        data_for_forecast = df[['Close']]  # Ajuste conforme as colunas que seu modelo espera
        
        # Normalizar os dados (supondo que o modelo tenha sido treinado com dados normalizados)
        scaler = MinMaxScaler(feature_range=(0, 1))
        normalized_data = scaler.fit_transform(data_for_forecast)

        # Preparar os dados para a entrada LSTM (reshape para [amostras, passos_de_tempo, características])
        time_steps = 60  # Ajuste conforme o que o seu modelo espera
        X = []

        for i in range(time_steps, len(normalized_data)):
            X.append(normalized_data[i - time_steps:i, 0])

        X = np.array(X)
        X = np.reshape(X, (X.shape[0], X.shape[1], 1))  # Garantir que os dados têm 3D como o LSTM espera
        
        # Fazer previsões
        forecasts = model.predict(X)
        
        # Desnormalizar as previsões para o valor original
        denormalized_predictions = scaler.inverse_transform(forecasts)
        

        # Preparar os dados para enviar no formato JSON
        results = []
        for i in range(len(denormalized_predictions)):
            results.append({
                "index": i,
                "data": df.index[i + time_steps].strftime('%Y-%m-%d'),  # Data da previsão
                "valor_real": data_for_forecast.iloc[i + time_steps].values[0],  # Valor real
                "previsao": float(denormalized_predictions[i][0]) # Valor previsto
            })

        return {
                "symbol": data.symbol,
                "forecasts": results
                }

    except Exception as e:
        return {"erro": f"Ocorreu um erro ao processar o modelo: {str(e)}"}


    