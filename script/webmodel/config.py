#Defining training parameters

home_dir='/content/'
model_dir = '/content/model'

logfile_webmodel= '/var/www/log/webmodellog.txt'
logfile_download='/var/www/log/download.txt'
logfile_wget= '/var/www/log/wget.txt'

file_cmd= '/var/www/cmd/cmdfile.txt'
script_dir='/content/webmodel/'

converter_srv='http://172.17.0.4/'
remote_path='model_web/'
download_URL=converter_srv+remote_path
tmp_dir='/content/tmp/'
download_dir=tmp_dir+remote_path
work_dir=home_dir+remote_path
token_in_file=download_dir+'token.txt'
out_dir = '/var/www/'
token_out_file=out_dir +'token.txt'

mysecret="mx4JncNOPY0ZwvU1B7re6KGH3GDTULs6"
