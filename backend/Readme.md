###
Создание базы данных
###
    sudo -u postgres psql
    create user roaddb with password 'roaddb';
    create database roaddb;
    grant all privileges on database roaddb to roaddb;
    ALTER ROLE roaddb SUPERUSER;
    \c roaddb;
    CREATE EXTENSION postgis;
    \q