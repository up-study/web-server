from .settings import *


REST_FRAMEWORK["DEFAULT_SCHEMA_CLASS"] = "drf_spectacular.openapi.AutoSchema"

INSTALLED_APPS.append("drf_spectacular")

SPECTACULAR_SETTINGS = {
    "TITLE": "Up-Study Application Server",
    "DESCRIPTION": "Up-Study exchange-education platform application server",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}
