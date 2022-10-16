#!/bin/zsh

sh scripts/export-schema.sh
docker build -t rapidoc . --file rapidoc.Dockerfile
docker run -p 2000:80 -d rapidoc
