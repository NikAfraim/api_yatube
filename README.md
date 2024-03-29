# Проект api_yatube

### Описание
Проект api_yatube основан на работе с API. \
Возможности для авторезированных пользователей:
- Посты:
    - создание,
    - редактирование,
    - удаление.
- Получения информации о сообществах.
- Комментарии:
    - создание,
    - редактирование,
    - удаление.
- Отслеживать активность других пользователей.\
Не авторезированные пользователи имеют доступ только на чтение.
---
# Технологии:
- Django 
- Django REST Framework
- djoser
- simplejwt.
---
Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/NikAfraim/api_yatube.git
```
```
cd api_yatube
```
---
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/bin/activate
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
---
Документация к проекту: http://127.0.0.1:8000/redoc/ \
Автор проекта: [NikAfraim](https://github.com/NikAfraim)
