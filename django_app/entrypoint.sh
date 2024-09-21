#!/bin/bash

python3 manage.py collectstatic --noinput
python3 manage.py ln -s staticfiles django_app/static
python3 -m http.server 9000 &
gunicorn --config gunicorn-cfg.py django_app.wsgi
