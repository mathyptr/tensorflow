FROM ubuntu:24.04
LABEL Augmentation Server for TensorFlow - Mathilde Patrissi Università di Firenze
RUN apt-get update	
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata curl git wget vim  unzip protobuf-compiler python3 python3-pip #python3-virtualenv

RUN mv /usr/lib/python3.12/EXTERNALLY-MANAGED /usr/lib/python3/EXTERNALLY-MANAGED.old
RUN (pip install pycocotools && pip install albumentations)

RUN (mkdir /content && mkdir /content/cmd && mkdir /content/cmd    && mkdir /content/log && chmod g+w /content/cmd  && mkdir /content/cgi-bin) 
WORKDIR /content

RUN ( wget  https://github.com/mathyptr/tensorflow/archive/refs/heads/master.zip && unzip -j  master.zip tensorflow-main/script/augmentation/* -d augmentation && rm master.zip && cp /content/augmentation/startcmd.py cgi-bin/ && chmod g+x /content/cgi-bin/startcmd.py)


