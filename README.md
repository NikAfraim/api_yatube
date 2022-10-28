# Проект api_final_yatube

### Описание
Проект api_final_yatube основан на работе с API. \
Здесь пользователи могут читать посты и оставлять свои на любую тему, а так же относить их к какой-то определенной группе. 
Пользователи так же могут писать комментарии под постами и подписываться на авторов, отслеживая их активность. 
Не авторезированные пользователи имеют доступ только на чтение.
---
## Технологии:
- Django 
- Django REST Framework
- djoser
- simplejwt.\
---
Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
https://github.com/NikAfraim/api_final_yatube.git
```
```
cd api_final_yatube
```
---
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source env/bin/activate
```
```
python3 -m pip install --upgrade pip
```
---
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
Документация к проекту: http://127.0.0.1:8000/redoc/ \
Автор проекта: NikAfraim
