FROM ubuntu:24.04
LABEL Server Web Model object for TensorFlow - Mathilde Patrissi Università di Firenze
RUN apt-get update	
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata git wget vim unzip python3 #protobuf-compiler python3-pip #python3-virtualenv


RUN (mkdir /content && mkdir /var/www && mkdir /var/www/cmd  && mkdir /var/www/log && chmod g+w /var/www/cmd  && mkdir /var/www/cgi-bin) 
WORKDIR /content


RUN wget  https://github.com/mathyptr/tensorflow/archive/refs/heads/master.zip 
RUN (unzip master.zip tensorflow-main/script/webmodel/* && mv tensorflow-main/script/webmodel . && cp /content/webmodel/startcmd.py /var/www/cgi-bin/ && chmod g+x /var/www/cgi-bin/startcmd.py)
RUN (rm master.zip && rm -r tensorflow-main)

RUN echo "python3 -m http.server --directory /var/www --cgi 80&" > /content/start.sh && echo "python3 webmodel/webmodel_main.py" >> /content/start.sh && chmod u+x /content/start.sh
#CMD /content/start.sh

EXPOSE 80
