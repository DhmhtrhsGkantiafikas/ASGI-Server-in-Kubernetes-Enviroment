import os

class Config:
    APP_VERSION = os.getenv("APP_VERSION", "1.0")

