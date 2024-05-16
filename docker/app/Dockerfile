FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /documents
WORKDIR /documents

COPY requirements.txt /documents
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY /app /documents/app

CMD ["python", "-m", "app.main"]
