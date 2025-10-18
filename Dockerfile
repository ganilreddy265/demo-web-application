FROM python:3.10-slim

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

EXPOSE 5000

ENV APP_ENV=local

CMD ["python", "app.py"]