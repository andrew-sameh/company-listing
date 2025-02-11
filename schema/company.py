from pydantic import BaseModel

class Company(BaseModel):
    cik: int 
    name: str
    ticker: str
    exchange: str