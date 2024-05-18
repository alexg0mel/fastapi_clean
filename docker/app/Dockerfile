FROM python:3.12

ARG SERVICE
ENV APP=app.$SERVICE.main
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /$SERVICE
WORKDIR /$SERVICE

COPY requirements.txt /$SERVICE
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY /app/$SERVICE /$SERVICE/app/$SERVICE
COPY /app/lib /$SERVICE/app/lib

CMD ["sh", "-c", "python -m $APP"]
