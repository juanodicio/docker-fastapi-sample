FROM python:3.9

WORKDIR /usr/src/app
COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--reload"]