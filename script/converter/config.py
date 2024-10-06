#Defining parameters

home_dir='/content/'
model_dir = '/content/model_web/'
inference_dir = '/content/inference_graph/saved_model'

logfile_converter= '/var/www/log/converterlog.txt'
logfile_download='/var/www/log/download.txt'
logfile_wget= '/var/www/log/wget.txt'

file_cmd= '/var/www/cmd/cmdfile.txt'
script_dir='/content/converter/'

tensorflow_srv='http://172.17.0.3/'
remote_path='inference_graph/'
download_URL=tensorflow_srv+remote_path
webmodel_srv='http://172.17.0.5/'
startcmd=webmodel_srv+'cgi-bin/startcmd.py'

work_dir=home_dir+remote_path
tmp_dir='/content/tmp/'
download_dir=tmp_dir+remote_path

token_in_file=download_dir+'token.txt'
out_dir = '/var/www/model_web/'
token_out_file=out_dir +'token.txt'

mysecret="mx4JncNOPY0ZwvU1B7re6KGH3GDTULs6"
