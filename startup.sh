# python manage.py collectstatic && gunicorn --workers 2 expenseWeb.wsgi
python manage.py collectstatic --noinput && gunicorn --workers 2 expenseWeb.wsgi:application
