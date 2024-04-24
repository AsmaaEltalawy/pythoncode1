FROM python:latest

RUN pip install nltk

WORKDIR /app

COPY . . 

CMD [ "python" , "main.py" ]