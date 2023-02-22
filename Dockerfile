# установка базового образа Python
FROM python:3.10-slim

# создание директории для приложения
RUN mkdir /app

# установка рабочей директории
WORKDIR /app

# копирование файла зависимостей проекта и установка зависимостей через pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# копирование кода проекта в контейнер
COPY . /app/

# запуск команды миграции базы данных
RUN python manage.py migrate

# открытие порта для веб-сервера Django
EXPOSE 8000

# запуск сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]