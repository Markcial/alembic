FROM debian:jessie
ENV environment=development
ENV PATH=$PATH:/Project/bin

RUN mkdir /Project
RUN apt-get -y update

# install base packages
RUN apt-get -y install bash vim curl wget
RUN apt-get -y install python python-pip
RUN apt-get -y install redis-tools
RUN apt-get -y install debian-keyring debian-archive-keyring

# install node and npm packages
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -
RUN apt-get update
RUN apt-get install -y nodejs
RUN npm install webpack -g

# install fish shell
RUN wget http://download.opensuse.org/repositories/shells:fish:release:2/Debian_8.0/Release.key; \
    apt-key add - < Release.key
RUN echo 'deb http://download.opensuse.org/repositories/shells:/fish:/release:/2/Debian_8.0/ /' >> /etc/apt/sources.list.d/fish.list
RUN apt-get update
RUN apt-get -y install fish

# install python packages
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

# install livereload development libraries
RUN npm install webpack-dev-server -g
RUN cd /Project/assets; npm install css-loader style-loader

# project configuration
ADD . /Project
RUN chmod a+x /Project/bin/*
RUN echo 'root:root' | chpasswd

# expose ports
EXPOSE 5000 5000
EXPOSE 8080 8080

# entrypoint in a shell
ENTRYPOINT /usr/bin/fish
