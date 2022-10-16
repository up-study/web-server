#!/bin/bash

upstudy collectstatic --noinput
upstudy migrate
"$@"
