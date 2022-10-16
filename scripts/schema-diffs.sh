#!/bin/zsh

. .venv/bin/activate
export DJANGO_SETTINGS_MODULE=src.upstudy.spectacular_settings

rm -f schema_before.json schema_after.json

git stash
upstudy spectacular --file schema_before.json --format openapi-json

git stash pop
upstudy spectacular --file schema_after.json --format openapi-json
