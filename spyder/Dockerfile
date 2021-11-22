FROM python:3.8


RUN apt-get update -y \
    && apt-get upgrade -y



RUN curl -sL https://deb.nodesource.com/setup_12.x |bash - \
    && apt-get install -y --no-install-recommends \
    wget \
    git \
    vim \
    curl \
    make \
    cmake \
    nodejs \
    python3 \
    python3-pip\
#    mysql-server \
    default-mysql-client \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf \
        /var/lib/apt/lists/* \
        /var/cache/apt/* \
        /usr/local/src/* \
        /tmp/*
       

RUN bash -c "$(wget -q -O - https://linux.kite.com/dls/linux/current)"

# install python library
COPY ./requirements.txt .
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt \
    && rm -rf ~/.cache/pip

# install jupyterlab & extentions
RUN pip3 install --upgrade --no-cache-dir \
    'jupyterlab~=3.0' \
    'jupyterlab-kite>=2.0.2' \
    jupyterlab_code_formatter \
    yapf \
    && rm -rf ~/.cache/pip \
    && jupyter labextension install \
      @hokyjack/jupyterlab-monokai-plus \
      @ryantam626/jupyterlab_code_formatter \
      @jupyterlab/toc \
      jupyterlab-vimrc \
      @axlair/jupyterlab_vim \ 
      @kiteco/jupyterlab-kite \
    && jupyter serverextension enable --py jupyterlab_code_formatter 


# google-chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
    echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list && \
    apt update && \
    apt-get install -y google-chrome-stable

# ChromeDriver
ADD https://chromedriver.storage.googleapis.com/77.0.3865.10/chromedriver_linux64.zip /opt/chrome/
RUN cd /opt/chrome/ && \
    unzip chromedriver_linux64.zip

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/chrome
ENV PYTHONPATH /home/work/library
#install jupyter-kite
#RUN cd && \
#    wget https://linux.kite.com/dls/linux/current && \
#    chmod 777 current && \
#    sed -i 's/"--no-launch"//g' current > /dev/null && \
#    ./current --install ./kite-installer

WORKDIR /home/work/


#build:
#      context: .
#      dockerfile: Dockerfile
