FROM python:3
USER root

WORKDIR /usr/src/app

RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./sample.py" ]