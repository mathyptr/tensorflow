FROM ubuntu
LABEL Custom object detection in the browser using TensorFlow.js - Mathilde Patrissi Università di Firenze
RUN apt-get update	
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata git wget vim  protobuf-compiler python3-pip #python3-virtualenv


RUN mkdir /content  
WORKDIR /content
CMD git clone https://github.com/mathyptr/tensorflow.git && chmod u+x tensorflow/configTensor.sh

