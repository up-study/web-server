# Up-Study Web Server
## Installation
```bash
git clone git@github.com:up-study/web-server.git
cd web-server

# setup database
# copy environment sample to `.env` and change values
cat env_sample > .env

# deploy using docker-compose
docker-compose up -d

# setup web-server
# ...
```

## Development
```bash
poetry install
pre-commit install
upstudy migrate

# export schema
sh scripts/export-schema.sh

# run rapidoc
sh scripts/run-rapidoc.sh

# look at the difference in schema after code changes
sh scripts/schema-diffs.sh
```
