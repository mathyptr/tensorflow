FROM tensorflow/tensorflow
LABEL Model Converter for TensorFlow.js - Mathilde Patrissi Università di Firenze
RUN apt-get update	
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata git wget vim  

RUN pip install tensorflowjs[wizard]

RUN (mkdir /content && mkdir /var/www && mkdir /var/www/cmd  && mkdir /var/www/log && chmod g+w /var/www/cmd && mkdir /var/www/cgi-bin) 
WORKDIR /content

RUN wget  https://github.com/mathyptr/tensorflow/archive/refs/heads/master.zip 
RUN (unzip master.zip tensorflow-main/script/converter/* && mv tensorflow-main/script/converter . && cp /content/converter/startcmd.py /var/www/cgi-bin/ && chmod g+x /var/www/cgi-bin/startcmd.py)
RUN (rm master.zip && rm -r tensorflow-main)

RUN echo "python3 -m http.server --directory /var/www --cgi 80&" > /content/start.sh && echo "python3 converter/converter_main.py" >> /content/start.sh && chmod u+x /content/start.sh
#CMD /content/start.sh


