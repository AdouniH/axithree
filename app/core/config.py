from pydantic import BaseModel


class Settings(BaseModel):
    project_name: str = "Axione API"
    api_v1_prefix: str = "/api/v1"


settings = Settings()
