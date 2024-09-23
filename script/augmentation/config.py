#Defining augmentation parameters

home_dir='/content'
image_coco_json='/content/images-aug/image_coco.json'
image_dir = '/content/images-aug'
imageout_dir = '/content/dataset/images'
num_iterations=10


logfile_augmentation= '/content/log/augmentation.txt'
logfile_download="/content/log/download.txt"
logfile_wget= '/content/log/wget.txt'
logfile_sendstartcmd="/content/log/sendstartcmd.txt"


file_cmd= '/content/cmd/cmdfile.txt'
script_dir='/content/augmentation/'


smartlens_srv='http://172.17.0.6:10000/'
remote_path='SmartLens-app/images-aug/'
download_URL=smartlens_srv+remote_path
tensorflow_srv='http://172.17.0.3/'
startcmd=tensorflow_srv+'cgi-bin/startcmd.py'

work_dir='/content/dataset/'
tmp_dir='/content/tmp/'
download_dir=tmp_dir+remote_path
token_in_file=tmp_dir+'token.txt'
out_dir='/content/dataset/'
token_out_file=out_dir +'token.txt'

mysecret="mx4JncNOPY0ZwvU1B7re6KGH3GDTULs6"

