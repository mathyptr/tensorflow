#Defining augmentation parameters

image_coco_json='/content/image/image_coco.json'
image_dir = '/content/image'
imageout_dir = '/content/dataset/images'
num_iterations=10


logfile_augmentation= '/content/log/augmentation.txt'
logfile_download="/content/log/download.txt"
logfile_wget= '/content/log/wget.txt'
logfile_sendstartcmd="/content/log/sendstartcmd.txt"


smartlens_srv='http://172.17.0.2/'
download_URL=smartlens_srv+'images/'
tensorflow_srv='http://172.17.0.3/'
startcmd=tensorflow_srv+'cgi-bin/startcmd.py'




