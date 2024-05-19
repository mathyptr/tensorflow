ln -s /usr/bin/python3 /usr/bin/python
cd /content
#git clone https://github.com/mathyptr/tensorflow.git 
git clone https://github.com/tensorflow/models.git 
wget https://raw.githubusercontent.com/hugozanini/object-detection/master/inferenceutils.py 
mv  ./tensorflow/labelmap.pbtxt /content 
mv ./tensorflow/kangaroodataset ./dataset 
wget http://download.tensorflow.org/models/object_detection/classification/tf2/20200710/mobilenet_v2.tar.gz 
tar -xvf mobilenet_v2.tar.gz 
wget https://raw.githubusercontent.com/tensorflow/models/master/research/object_detection/configs/tf2/ssd_mobilenet_v2_320x320_coco17_tpu-8.config 
mv ssd_mobilenet_v2_320x320_coco17_tpu-8.config mobilenet_v2.config 
cd /content/models/research/
protoc object_detection/protos/*.proto --python_out=.
cp object_detection/packages/tf2/setup.py .
mv /usr/lib/python3.12/EXTERNALLY-MANAGED /usr/lib/python3.12/EXTERNALLY-MANAGED.old
#il successivo comando da errore indicando la necessità di una versione di python <3.12,>=3.8
python -m pip install .

#WORKDIR /content
# Test the TensorFlow Object Detection API
#CMD python models/research/object_detection/builders/model_builder_tf2_test.py

#CMD python dataset/generate_tf_records.py -l /content/labelmap.pbtxt -o dataset/train.record -i dataset/images -csv dataset/train_labels.csv
#CMD python dataset/generate_tf_records.py -l /content/labelmap.pbtxt -o dataset/test.record -i dataset/images -csv dataset/test_labels.csv

