from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # CORE SETTINGS
    ENV: str = "DEV"
    PROJECT_NAME: str = "FastAPI Backend"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "Backend Technical Interview"

    PUBLIC_COMPANIES_API_URL: str = 'https://www.sec.gov/files/company_tickers_exchange.json'
    
    model_config = SettingsConfigDict(
        env_file=".env", case_sensitive=True
    )


settings: Settings = Settings() 
