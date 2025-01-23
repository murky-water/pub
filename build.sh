#!/bin/bash
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput
python3 manage.py makemigrations sea
python3 manage.py migrate sea
python3 manage.py loaddata db_data
