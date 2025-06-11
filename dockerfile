FROM python:3.11

WORKDIR /app

COPY requirements.txt requirements.txt 
RUN pip install --no-cache-dir -r requirements.txt


COPY pagination_example ./pagination_example
COPY . .
CMD ["python3", "manage.py", "runserver"]

