# Тестовое задание геймдева
## Как запустить локально
1. Создайте и активируйте виртуальное окружение:
```
python3 -m venv .venv
. .venv/bin/activate
```
2. Установите зависимости
```
pip3 install --upgrade pip
pip3 install -r app/requirements.txt
```
3. Создайте файл `.env` и заполните его по аналогии с `.env.template`
4. Примените миграции:
```
python3 app/manage.py migrate
```
5. Создайте супер пользователя:
```
python3 app/manage.py createsuperuser
```
6. Запустите джанго:
```
python3 app/manage.py runserver 8000
```
