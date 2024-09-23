

from config import *


augmented_file=imageout_dir+'/augmented_files.csv'

nlines=0
for line in open(augmented_file):
    nlines+=1

nlines-=1

train_file=imageout_dir+'/train_labels.csv'
test_file=imageout_dir+'/test_labels.csv'

ftrain = open(train_file, "w")
ftest = open(test_file, "w")
header_csv = 'filename,width,height,class,xmin,ymin,xmax,ymax,source' 
                   
ftest.writelines(header_csv)
i=0
for line in open(augmented_file):
    if i<=nlines*80/100 :
        ftrain.writelines(line)
    else:
        ftest.writelines(line)
    i+=1

ftrain.close()
ftest.close()
