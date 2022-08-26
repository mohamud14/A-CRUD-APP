# FROM python:3.8
# RUN apt-get update
# RUN apt-get install -y python
# WORKDIR /code
# COPY . .
# RUN pip install -r requirements.txt
# EXPOSE 5000
# ENTRYPOINT ["python"]
# CMD ["main.py"]

FROM python:3.6-alpine
EXPOSE 5000
WORKDIR /app
ENV SQLALCHEMY_DATABASE_URI="sqlite:///data.db"
RUN python-mpip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT main.py
