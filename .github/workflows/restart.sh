#!/bin/sh
cd Site/Integrador-6-Periodo
source venv/bin/activate
git pull
pip install -r requirements.txt
python3 manage.py migrate
systemctl restart gunicorn
systemctl restart nginx