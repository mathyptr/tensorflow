from config import *
import random 

augmented_file=imageout_dir+'/augmented_files.csv'
train_file=work_dir+'/train_labels.csv'
test_file=work_dir+'/test_labels.csv'

f = open(augmented_file,'r')
header_csv = f.readline()
lines = f.readlines()
f.close()


nlines=len(lines)
random.shuffle(lines) 
ftrain = open(train_file, "w")
ftest = open(test_file, "w")

ftrain.writelines(header_csv)                   
ftest.writelines(header_csv)

i=0
for line in lines:
    if i<=nlines*80/100 :
        ftrain.writelines(line)
    else:
        ftest.writelines(line)
    i+=1

ftrain.close()
ftest.close()
