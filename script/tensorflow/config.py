#Defining training parameters

home_dir='/content/'
train_record_path = '/content/dataset/train.record'
test_record_path = '/content/dataset/test.record'
model_dir = '/content/training/'
labelmap_path = '/content/labelmap.pbtxt'


file_train_labels='train_labels.csv'
file_test_labels='test_labels.csv'

train_labels='/content/dataset/train_labels.csv'
test_labels='/content/dataset/test_labels.csv'
dataset_images='/content/dataset/images'

pipeline_config_path = '/content/mobilenet_v2.config'
fine_tune_checkpoint = '/content/mobilenet_v2/mobilenet_v2.ckpt-1'
#fine_tune_checkpoint = '/content/training_checkpoint/ckpt-1'
#fine_tune_checkpoint = '/content/training_checkpoint/ckpt-3'
fine_tune_checkpoint_type= 'classification'
#fine_tune_checkpoint_type= 'detection'


output_directory = 'inference_graph'

logfile_training="/content/log/traininglog.txt"
logfile_validate="/content/log/validatelog.txt"
logfile_export="/content/log/exportlog.txt"
logfile_download="/content/log/download.txt"
logfile_wget= '/content/log/wget.txt'
logfile_sendstartcmd="/content/log/sendstartcmd.txt"

file_cmd= '/content/cmd/cmdfile.txt'
script_dir='/content/tensorflow/'

augmentation_srv='http://172.17.0.2/'
remote_path='dataset/'
download_URL=augmentation_srv+remote_path
converter_srv='http://172.17.0.4/'
startcmd=converter_srv+'cgi-bin/startcmd.py'

work_dir=home_dir+remote_path
tmp_dir='/content/tmp/'
download_dir=tmp_dir+remote_path


token_in_file=download_dir+'token.txt'
out_dir='/content/inference_graph/'
token_out_file=out_dir +'token.txt'


mysecret="mx4JncNOPY0ZwvU1B7re6KGH3GDTULs6"


