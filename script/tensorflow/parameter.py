import re

from config import *



#Defining training parameters
num_classes = 7
batch_size = 34
num_steps = 100
num_eval_steps = 00


def setConfigFile():
 with open(pipeline_config_path) as f:
    config = f.read()

 with open(pipeline_config_path, 'w') as f:
  # Set labelmap path
  config = re.sub('label_map_path: ".*?"','label_map_path: "{}"'.format(labelmap_path), config)
  # Set fine_tune_checkpoint path
  config = re.sub('fine_tune_checkpoint: ".*?"','fine_tune_checkpoint: "{}"'.format(fine_tune_checkpoint), config)
  # Set fine_tune_checkpoint_type 
  config = re.sub('fine_tune_checkpoint_type: ".*?"','fine_tune_checkpoint_type: "{}"'.format(fine_tune_checkpoint_type), config)
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


