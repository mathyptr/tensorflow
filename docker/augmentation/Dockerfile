FROM ubuntu:24.04
LABEL Augmentation Server for TensorFlow - Mathilde Patrissi Università di Firenze
RUN apt-get update	
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata curl git wget vim  unzip python3 python3-pip

RUN mv /usr/lib/python3.12/EXTERNALLY-MANAGED /usr/lib/python3/EXTERNALLY-MANAGED.old
RUN (pip install pycocotools && pip install albumentations)

RUN (mkdir /content && mkdir /content/image && mkdir /content/dataset && mkdir /content/cmd && mkdir /content/log && chmod g+w /content/cmd  && mkdir /content/cgi-bin) 
WORKDIR /content


RUN wget  https://github.com/mathyptr/tensorflow/archive/refs/heads/master.zip

RUN (unzip master.zip tensorflow-main/script/augmentation/* && mv tensorflow-main/script/augmentation . && cp /content/augmentation/startcmd.py cgi-bin/ && chmod g+x /content/cgi-bin/startcmd.py)
RUN (rm master.zip && rm -r tensorflow-main)

RUN echo "python3 -m http.server --cgi 80&" > /content/start.sh && echo "python3 augmentation/augmentation_main.py" >> /content/start.sh && chmod u+x /content/start.sh
#CMD /content/start.sh


EXPOSE 80
