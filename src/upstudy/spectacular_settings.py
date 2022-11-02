from .settings import *  # noqa[f403]


REST_FRAMEWORK[  # noqa[f405]
    "DEFAULT_SCHEMA_CLASS"
] = "drf_spectacular.openapi.AutoSchema"

INSTALLED_APPS.append("drf_spectacular")  # noqa[f405]

SPECTACULAR_SETTINGS = {
    "TITLE": "Up-Study Application Server",
    "DESCRIPTION": "Up-Study exchange-education platform application server",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "COMPONENT_NO_READ_ONLY_REQUIRED": True,
    "POSTPROCESSING_HOOKS": [
        "drf_spectacular.hooks.postprocess_schema_enums",
        "drf_spectacular.contrib.djangorestframework_camel_case.camelize_serializer_fields",
    ],
}
