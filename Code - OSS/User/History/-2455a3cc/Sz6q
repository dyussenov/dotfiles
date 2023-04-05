FROM python:3.9
RUN mkdir /race-ms
WORKDIR /race-ms
COPY . /race-ms
RUN pip install -r requirements.txt
WORKDIR /race-ms/database
RUN python3 -m create_db
WORKDIR /race-ms
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]