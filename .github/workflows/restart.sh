#!/bin/sh
cd /root/Site/Integrador-6-Periodo
source venv/bin/activate
git pull
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic --noinput
systemctl restart gunicorn
systemctl restart nginx