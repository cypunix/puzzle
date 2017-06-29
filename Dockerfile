FROM python:2.7
RUN apt-get update && apt-get install -y \
  git

RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN git clone https://github.com/cypunix/puzzle.git
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
