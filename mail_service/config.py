from pydantic import EmailStr, SecretStr, Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    smtp_server: str = Field(..., env="SMTP_SERVER")
    smtp_port: int = Field(..., env="SMTP_PORT")
    smtp_user: EmailStr = Field(..., env="SMTP_USER")
    smtp_password: SecretStr = Field(..., env="SMTP_PASSWORD")
    use_tls: bool = Field(default=True)
    use_ssl: bool = Field(default=False)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
