# Use an official Python runtime as a parent image
FROM python:3.12
RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2
WORKDIR /app
COPY data-processing.py data-processing.py

ENTRYPOINT [ "python", "data-processing.py"]

