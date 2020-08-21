# import os
from os import listdir


with open("D:/non-dropbox-files/research/looking-at-animals-training-data/training-data-2020-07-02-Camera6/output-2020-07-02-Camera6.txt", "w+") as a:
    # for files in os.walk(r'D:\non-dropbox-files\research\looking-at-animals-captured-images\2020-07-02-Camera3'):
    a.write("ID, image, species, count" + "\n")
    IDCount = 1
    for files in listdir("D:/non-dropbox-files/research/looking-at-animals-captured-images/2020-07-02-Camera6/"):
        # for filename in files:
        a.write(str(IDCount) + "," + str(files) + ",," + "\n") 
        IDCount +=1
            # f = os.path.join(path, filename)
            # a.write(str(filename) + os.linesep) 
            # print(filename)
            