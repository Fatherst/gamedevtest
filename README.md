# Тестовое задание геймдева
## Как запустить локально
1. Создайте и активируйте виртуальное окружение:
```
python -m venv .venv
. .venv/bin/activate
```
2. Установите зависимости
```
pip install --upgrade pip
pip install -r app/requirements.txt
```
3. Создайте файл `.env` и заполните его по аналогии с `.env.template`
4. Примените миграции:
```
python manage.py migrate
```
5. Создайте супер пользователя:
```
python manage.py createsuperuser
```
6. Запустите джанго:
```
python manage.py runserver
```
