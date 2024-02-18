FROM python:3.8

WORKDIR /home/links_django
COPY requirements.txt /home/links_django
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./links_django /home/links_django

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
