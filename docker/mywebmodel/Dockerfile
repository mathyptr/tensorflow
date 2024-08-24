FROM ubuntu:24.04
LABEL Server Web Model object for TensorFlow - Mathilde Patrissi Università di Firenze
RUN apt-get update	
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata git wget vim  protobuf-compiler python3 #python3-pip #python3-virtualenv



RUN (mkdir /content && mkdir /content/cmd    && mkdir /content/log && chmod g+w /content/cmd) 
WORKDIR /content


