FROM python:3.8.5-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN pip install --upgrade pip

RUN apk add --update --no-cache g++ gcc libxslt-dev

RUN python -m venv venv
CMD ["source", "venv/bin/activate"]

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

RUN adduser -D myuser
USER myuser

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]