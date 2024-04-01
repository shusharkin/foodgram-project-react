
### Краткое описание проекта:

Cайт Foodgram, «Продуктовый помощник».
На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Шаблон наполнения env-файла:

```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

### Описание команд для запуска приложения в контейнерах:

Сборка и запуск контейнеров из директории ./infra:

```
docker-compose up -d
```

Остановка контейнеров:

```
docker-compose down -v 
```

### Описание команды для заполнения базы данными:

```
python manage.py csv_import
```

### Технологии:

Проект сделан на Django и DRF. Django-проект работает на веб-сервере nginx через WSGI-сервер Gunicorn. База данных - PostgreSQL.  

Суперюзер:  
login: admin  
pass: admin  
e-mail: test@test.test  

### Об авторе:

Автор: Шушаркин Герман (ссылка на GitHub https://github.com/shusharkin).
