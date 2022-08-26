FROM python:3.8
RUN apt-get update
RUN apt-get install -y python
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["main.py"]
