import sys
import glob
import errno

path = 'D:/non-dropbox-files/research/looking-at-animals-captured-images/2020-07-09-Camera5/*.jpg'

files = glob.glob(path)   
# open("D:/non-dropbox-files/research/looking-at-animals-code/create-inventory/datalog-combined-2020-07-09-Camera5.txt", 'w+')
for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
   with open('D:/non-dropbox-files/research/looking-at-animals-code/1-create-inventory/datalog-combined-2020-07-09-Camera5.txt', 'w+') as out_file:
	   out_file.write(name)
      
print ('process 1 complete')