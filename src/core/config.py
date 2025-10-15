import os

from pydantic_settings import BaseSettings

class Config(BaseSettings):
    ENV: str = os.getenv("ENV", "dev")
    
    ## Database settings
    MONGO_MAX_POOL: int = int(os.getenv("MONGO_MAX_POOL", "100"))
    MONGO_MIN_POOL: int = int(os.getenv("MONGO_MIN_POOL", "10"))
    
    MONGO_URI: str = os.getenv("MONGO_URI",
                               f"mongodb://tnv_staging:weUzrkexM5iL@192.168.60.21:27017,192.168.60.22:27017,192.168.60.23:27017,192.168.60.24:27017/?retryWrites=true&replicaSet=tnv_dev&authSource=tnv_staging&authMechanism=SCRAM-SHA-1")
    MONGO_DB_NAME: str = os.getenv("MONGO_DB_NAME", 'tnv_staging')
    

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
    