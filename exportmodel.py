with open('/usr/local/lib/python3.9/site-packages/tensorflow/python/keras/utils/tf_utils.py') as f:
#with open('/usr/local/lib/python3.6/dist-packages/tensorflow/python/keras/utils/tf_utils.py') as f:
    tf_utils = f.read()

with open('/usr/local/lib/python3.9/site-packages/tensorflow/python/keras/utils/tf_utils.py', 'w') as f:
#with open('/usr/local/lib/python3.6/dist-packages/tensorflow/python/keras/utils/tf_utils.py', 'w') as f:
  # Set labelmap path
  throw_statement = "raise TypeError('Expected Operation, Variable, or Tensor, got ' + str(x))"
  tf_utils = tf_utils.replace(throw_statement, "if not isinstance(x, str):" + throw_statement)
  f.write(tf_utils)

output_directory = '/content/inference_graph'
