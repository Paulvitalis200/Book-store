from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator


class Settings(BaseSettings):
    DATABASE_URL: str 
    
    @field_validator('DATABASE_URL')
    @classmethod
    def validate_database_url(cls, v: str) -> str:
        """Ensure DATABASE_URL uses async driver for PostgreSQL"""
        if v.startswith('postgresql://'):
            # Replace with asyncpg driver for async operations
            return v.replace('postgresql://', 'postgresql+asyncpg://', 1)
        return v

    model_config = SettingsConfigDict(
        env_file=".env", 
        extra="ignore"
    )

Config = Settings()