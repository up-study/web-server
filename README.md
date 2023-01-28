# Up-Study Web Server
## Installation
```bash
git clone git@github.com:up-study/web-server.git
cd web-server

# setup database
# copy environment sample to `.env` and change values
cat env_sample > .env

# deploy using docker-compose
docker-compose up --build -d db cache
# ...
```

## Development
```bash
python3 -m venv .venv
. .venv/bin/activate

poetry install
pre-commit install
upstudy migrate
```
