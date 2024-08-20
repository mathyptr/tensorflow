FROM ubuntu:24.04
LABEL Custom object detection using TensorFlow.js - Mathilde Patrissi Università di Firenze
RUN apt-get update	
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata git wget vim  protobuf-compiler build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev curl software-properties-common


RUN mkdir /content  
WORKDIR /content


RUN (wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tar.xz && tar -xf Python-3.9.0.tar.xz && cd Python-3.9.0 && ./configure && make altinstall)
RUN ln -s /usr/local/bin/python3.9 /usr/local/bin/python


RUN cd /content  
RUN git clone https://github.com/mathyptr/tensorflow.git
RUN (mv ./tensorflow/labelmap.pbtxt /content && mv ./tensorflow/kangaroodataset ./dataset && mv  ./tensorflow/models .) 
RUN (wget http://download.tensorflow.org/models/object_detection/classification/tf2/20200710/mobilenet_v2.tar.gz  && tar -xvf mobilenet_v2.tar.gz )
RUN (wget https://raw.githubusercontent.com/tensorflow/models/master/research/object_detection/configs/tf2/ssd_mobilenet_v2_320x320_coco17_tpu-8.config && mv ssd_mobilenet_v2_320x320_coco17_tpu-8.config mobilenet_v2.config)

RUN (cd /content/models/research/ && protoc object_detection/protos/*.proto --python_out=.)
RUN (cd /content/models/research/ && cp object_detection/packages/tf2/setup.py . && mv /usr/lib/python3.12/EXTERNALLY-MANAGED /usr/lib/python3.12/EXTERNALLY-MANAGED.old && python -m pip install .)

RUN pip3.9 install tensorflow==2.13.1

RUN python /content/models/research/object_detection/builders/model_builder_tf2_test.py

