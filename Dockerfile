FROM python:3.11.8

WORKDIR /usr/src/app

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "backend/query.py"]
