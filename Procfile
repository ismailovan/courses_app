web: gunicorn courses_app.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate