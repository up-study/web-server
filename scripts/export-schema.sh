#!/bin/zsh

export DJANGO_SETTINGS_MODULE=src.upstudy.spectacular_settings

rm -f schema.yml schema.json

upstudy spectacular --file schema.yml
upstudy spectacular --file schema.json --format openapi-json
