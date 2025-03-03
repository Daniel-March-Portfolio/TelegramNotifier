#!/bin/bash
set -a;
source .env;
set +a;
python3 manage.py migrate;
exec python3 manage.py runserver 0.0.0.0:8000;