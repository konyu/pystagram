FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN mkdir /root/app

RUN apt-get install -y vim
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN pip install instagram-scraper

# TODO PIP install したライブラリをインポートする
WORKDIR /root
#COPY Pipfile ./
#RUN pipenv install