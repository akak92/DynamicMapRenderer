FROM ubuntu:22.04

RUN mkdir /app

WORKDIR /app

RUN mkdir /app/results

RUN apt-get update
RUN apt-get install python3-mapnik -y
RUN apt install python3-pip -y
RUN pip install python-dotenv
RUN pip install tweepy
RUN pip install requests
RUN pip install pillow
RUN pip install pytz
RUN apt-get update
RUN pip install mapnik
COPY . .

CMD ["sh", "/app/run.sh"]
