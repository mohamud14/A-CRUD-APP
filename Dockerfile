# FROM python:3.8
# RUN apt-get update
# RUN apt-get install -y python
# WORKDIR /code
# COPY . .
# RUN pip install -r requirements.txt
# EXPOSE 5000
# ENTRYPOINT ["python"]
# CMD ["main.py"]
#
# FROM python:3.6-alpine
# COPY . .
# WORKDIR /A-CRUD-APP
# ENV SQLALCHEMY_DATABASE_URI="sqlite:///data.db"
# RUN python -m pip install --upgrade pip
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# EXPOSE 5000
# ENTRYPOINT ["python"]
# CMD ["main.py"]

FROM python:3.10-alpine

EXPOSE 8000

WORKDIR /app
ENV db_connection="sqlite:///data.db"

# install dependencies
RUN apk add build-base && \
    python -m pip install --upgrade pip
COPY requirements.txt .

# install requirements
RUN pip install -r requirements.txt --no-cache-dir
COPY . .

ENTRYPOINT python -u app.py