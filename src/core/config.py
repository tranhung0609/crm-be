import os

from pydantic_settings import BaseSettings

class Config(BaseSettings):
    ENV: str = os.getenv("ENV", "dev")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "2490242a5be290aec70e1a9ec322835512b500a077f9077b8fbfc41530ab59b18beffbbf44fb1564fc40b6095cbb15c8f4f71fcc14765174ccf0427f68254477")
    ## Database settings
    MONGO_MAX_POOL: int = int(os.getenv("MONGO_MAX_POOL", "100"))
    MONGO_MIN_POOL: int = int(os.getenv("MONGO_MIN_POOL", "10"))
    
    MONGO_URI: str = os.getenv("MONGO_URI",
                               f"mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.5.8")
    MONGO_DB_NAME: str = os.getenv("MONGO_DB_NAME", 'crm')

class DevelopmentConfig(Config):
    pass


class LocalConfig(Config):
    pass


class ProductionConfig(Config):
    pass


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "dev": DevelopmentConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
    