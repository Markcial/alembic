FROM debian:jessie
ENV environment=development
ENV PATH=$PATH:/Project/bin

RUN mkdir /Project
RUN apt-get -y update
RUN apt-get -y install bash
RUN apt-get -y install vim
RUN apt-get -y install python
RUN apt-get -y install python-pip
RUN apt-get -y install wget
RUN wget http://download.opensuse.org/repositories/shells:fish:release:2/Debian_8.0/Release.key; \
    apt-key add - < Release.key
RUN echo 'deb http://download.opensuse.org/repositories/shells:/fish:/release:/2/Debian_8.0/ /' >> /etc/apt/sources.list.d/fish.list
RUN apt-get update
RUN apt-get -y install fish
RUN pip install flask
RUN pip install redis
RUN pip install gunicorn
RUN pip install minimock
RUN pip install nose
RUN apt-get -y install unzip
RUN cd /usr/lib/python2.7/dist-packages/; \
    wget -c "https://raw.githubusercontent.com/emmetio/pyv8-binaries/master/pyv8-linux64.zip"; \
    unzip pyv8-linux64.zip; \
    rm pyv8-linux64.zip
RUN pip install PyReact
RUN apt-get -y install redis-tools
ADD . /Project
RUN chmod a+x /Project/bin/*
RUN echo 'root:root' | chpasswd
EXPOSE 5000

ENTRYPOINT /usr/bin/fish