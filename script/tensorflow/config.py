#Defining training parameters

train_record_path = '/content/dataset/train.record'
test_record_path = '/content/dataset/test.record'
model_dir = '/content/training/'
labelmap_path = '/content/labelmap.pbtxt'

train_labels='/content/dataset/train_labels.csv'
test_labels='/content/dataset/test_labels.csv'
dataset_images='/content/dataset/images'

pipeline_config_path = '/content/mobilenet_v2.config'
fine_tune_checkpoint = '/content/mobilenet_v2/mobilenet_v2.ckpt-1'

output_directory = 'inference_graph'

logfile_training="/content/log/traininglog.txt"
logfile_validate="/content/log/validatelog.txt"
logfile_export="/content/log/exportlog.txt"
logfile_download="/content/log/download.txt"
logfile_sendstartcmd="/content/log/sendstartcmd.txt"


augmentation_srv='http://172.17.0.2/'
download_URL=augmentation_srv+'dataset'
converter_srv='http://172.17.0.4/'
startcmd=converter_srv+'cgi-bin/startcmd.py'


