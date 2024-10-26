from pydantic import EmailStr, SecretStr, Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_host: str = Field(..., env="DB_HOST", default="localhost")
    db_port: int = Field(..., env="DB_PORT", default=5432)
    db_user: str = Field(..., env="DB_USER", default="postgres")
    db_password: SecretStr = Field(..., env="DB_PASSWORD", default="postgres")
    db_name: str = Field(..., env="DB_NAME", default="postgres")
    db_type: str = Field(..., env="DB_TYPE", default="postgresql")
    db_driver: str = Field(..., env="DB_DRIVER", default="asyncpg")

    token_expire: int = Field(..., env="TOKEN_EXPIRE", default=300)

    redis_host: str = Field(..., env="REDIS_HOST", default="localhost")
    redis_port: int = Field(..., env="REDIS_PORT", default=6379)
    redis_db: int = Field(..., env="REDIS_DB", default=0)

    redis_storage: str = f"redis://{redis_host}:{redis_port}/{redis_db}"

    sql_alchemy_database_url: str = f"""{db_type}+{db_driver}://
                                        {db_user}:{db_password}@
                                        {db_host}:{db_port}/{db_name}"""
    
    jwt_secret: SecretStr = Field(..., env="JWT_SECRET")
    jwt_expire: int = Field(..., env="JWT_EXPIRE", default=30)
    jwt_algorithm: str = Field(..., env="JWT_ALGORITHM", default="HS256")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings() 
