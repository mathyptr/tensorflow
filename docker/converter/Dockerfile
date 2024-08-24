FROM tensorflow/tensorflow
LABEL Model Converter for TensorFlow.js - Mathilde Patrissi Università di Firenze
RUN apt-get update	
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata git wget vim  

RUN pip install tensorflowjs[wizard]

RUN (mkdir /content && mkdir /content/cmd    && mkdir /content/log && chmod g+w /content/cmd) 
WORKDIR /content

