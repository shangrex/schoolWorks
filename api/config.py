import os


class Config:
    """Service configurations"""
    APP_TITLE = os.environ.get("APP_TITLE", "School backend")
    APP_DESCRIPTION = os.environ.get("APP_DESCRIPTION", "School backend")
    VERSION = os.environ.get("VERSION", "0.0.0")
    OPENAPI_URL = os.environ.get("OPENAPI_URL", "/openapi.json")
