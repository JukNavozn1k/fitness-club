<br />
<div align="center">
  <a href="#">
    <img src="https://cdn-icons-png.flaticon.com/512/952/952816.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Fitness Club</h3>

  <p align="center">
    Fast & Smart GYM app!
    <br/>
    <a href="#"><strong>Последний релиз!</strong></a>
    <br />
    <br />
    <a href="#">Демо</a>
    ·
    <a href="#">Сообщить об ошибке</a>
    ·
  </p>
</div>



# О проекте

## Описание
Данный проект создан в целях написания курсовой работы

## Карта обновлений

ToDo



## Инструкция по запуску
### DEV 
1. Устанавливаем переменные окружения в файле .env

Пример файла .env показан ниже

```
DB_NAME=gg
DB_USER=gleb
DB_PASS=1234
DB_HOST=db
DB_PORT=5432

TEST_DB_NAME=gg_test
TEST_DB_USER=gleb_test
TEST_DB_PASS=1234
TEST_DB_HOST=db_test
TEST_DB_PORT=5430

MONGO_INITDB_ROOT_USERNAME=mongoadmin
MONGO_INITDB_ROOT_PASSWORD=secret
MONGO_PORT=27017
```

2. Запускаем docker-compose

```
docker-compose up
```

3. Применяем миграции 

```
docker-compose exec backend alembic upgrade head
```

После создания образа и запуска compose файла должен быть запущен backend-сервер на порту 8000.
Проверку работоспособности можно выполнить перейдя на: http://localhost:8000/docs

Frontend сервер работает на 3000 порту (http://localhost:3000)