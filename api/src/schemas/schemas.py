from pydantic import BaseModel


class FinancyDataSchema(BaseModel):
    symbol: str
    start_date: str  
    end_date: str

    class Config:
        json_schema_extra = {
            "example": {
                "symbol": "DIS",
                "start_date": "2023-02-11",
                "end_date": "2025-02-11"
            }
        }
