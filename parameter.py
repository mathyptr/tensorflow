import re

#Defining training parameters
num_classes = 1
batch_size = 10
num_steps = 100
num_eval_steps = 1000

train_record_path = '/content/dataset/train.record'
test_record_path = '/content/dataset/test.record'
model_dir = '/content/training/'
labelmap_path = '/content/labelmap.pbtxt'

train_labels='/content/dataset/train_labels.csv'
test_labels='/content/dataset/test_labels.csv'
dataset_images='/content/dataset/images'

pipeline_config_path = 'mobilenet_v2.config'
fine_tune_checkpoint = '/content/mobilenet_v2/mobilenet_v2.ckpt-1'

output_directory = 'inference_graph'

def setConfigFile():
 with open(pipeline_config_path) as f:
    config = f.read()

 with open(pipeline_config_path, 'w') as f:
  # Set labelmap path
  config = re.sub('label_map_path: ".*?"','label_map_path: "{}"'.format(labelmap_path), config)
  # Set fine_tune_checkpoint path
  config = re.sub('fine_tune_checkpoint: ".*?"','fine_tune_checkpoint: "{}"'.format(fine_tune_checkpoint), config)
  # Set train tf-record file path
  config = re.sub('(input_path: ".*?)(PATH_TO_BE_CONFIGURED/train)(.*?")','input_path: "{}"'.format(train_record_path), config)
  # Set test tf-record file path
  config = re.sub('(input_path: ".*?)(PATH_TO_BE_CONFIGURED/val)(.*?")','input_path: "{}"'.format(test_record_path), config)
  # Set number of classes.
  config = re.sub('num_classes: [0-9]+','num_classes: {}'.format(num_classes), config)
  # Set batch size
  config = re.sub('batch_size: [0-9]+','batch_size: {}'.format(batch_size), config)
  # Set training steps
  config = re.sub('num_steps: [0-9]+','num_steps: {}'.format(num_steps), config)
  f.write(config)


if __name__ == '__main__':
 setConfigFile()


