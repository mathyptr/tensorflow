#Defining training parameters

model_dir = '/content/model_web'
inference_dir = '/content/inference_graph/saved_model'
logfile_converter= '/content/log/converterlog.txt'
logfile_download="/content/log/download.txt"
logfile_wget= '/content/log/wget.txt'

tensorflow_srv='http://172.17.0.3/'
download_URL=tensorflow_srv+'inference_graph'
webmodel_srv='http://172.17.0.4/'
startcmd=webmodel_srv+'cgi-bin/startcmd.py'
