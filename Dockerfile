FROM python:3.10-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

# CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "shop_project.asgi:application"]
CMD ["python", "manage.py", "runserver"]