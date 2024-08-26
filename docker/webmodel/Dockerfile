FROM ubuntu:24.04
LABEL Server Web Model object for TensorFlow - Mathilde Patrissi Università di Firenze
RUN apt-get update	
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata git wget vim unzip python3 #protobuf-compiler python3-pip #python3-virtualenv



RUN (mkdir /content && mkdir /content/cmd  && mkdir /content/log && chmod g+w /content/cmd  && mkdir /content/cgi-bin) 
WORKDIR /content
RUN ( wget  https://github.com/mathyptr/tensorflow/archive/refs/heads/master.zip && unzip -j  master.zip tensorflow-main/script/webmodel/* -d webmodel && rm master.zip && cp /content/webmodel/startcmd.py cgi-bin/ && chmod g+x /content/cgi-bin/startcmd.py)


