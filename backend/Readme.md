###
Установите базу Postgres.   
Для создание базы данных введите следующие команды
###
    sudo -u postgres psql
    create user roaddb with password 'roaddb';
    create database roaddb;
    grant all privileges on database roaddb to roaddb;
    ALTER ROLE roaddb SUPERUSER;
    \c roaddb;
    CREATE EXTENSION postgis;
    \q

###
Для запуска сервера.
###
    python3 -m venv venv
    source venv/bin/activate 
       or
    venv\Scripts\activate # для windows

    pip install -r requirements.txt
    python3 manage.py runserver --settings=backend.settings.local