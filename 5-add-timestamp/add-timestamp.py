import csv
import os.path
import time
from datetime import datetime

'''
Reads the last modified date of image files from a csv
and writes a new CSV file with these times added 
Also adds image folder and image filename as separate fields 

date: August 14 2020 
'''

# edit these variables
training_run = "training-run-8/"

# do not edit these variables
my_csv = "combined-files.csv"
my_edited_csv = "combined-files-times.csv"
my_csv_path = "D:/non-dropbox-files/research/looking-at-animals-training-runs/" + training_run + "my-data/" + my_csv
my_edited_csv_path = "D:/non-dropbox-files/research/looking-at-animals-training-runs/" + training_run + "my-data/" + my_edited_csv

"""
function that receives an integer and adds '0' at the beginning
if the integer has exactly one digit
parameter: integer
returns: string

"""
def two_digit(my_int):
    my_str = str(my_int) 
    if len(my_str) == 1:
        my_str = "0" + my_str
        return (my_str)
    else:
        return (str(my_int))



with open(my_csv_path, "r") as infile, open(my_edited_csv_path, "w", newline='') as outfile:
    readCSV = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(readCSV)
    if header != None:
        header.insert(2,"time")
        header.insert(2,"date")
        header.insert(2,"timestamp")
        header.insert(2,"folder")
        header.insert(2,"imagename")
        writer.writerow(header)
    
    for row in readCSV:
        my_path =  row[1]
        if os.path.isfile(my_path):
            my_time = str(time.ctime(os.path.getmtime(my_path)))
            dt_object = datetime.fromtimestamp(os.path.getmtime(my_path))
            row.insert(2,str(two_digit(dt_object.hour)) +":"+ str(two_digit(dt_object.minute)) +":"+ str(two_digit(dt_object.second)))
            row.insert(2,dt_object.strftime("%Y-%m-%d"))
            row.insert(2,str(dt_object))
            my_filename = os.path.basename(my_path)
            # row.insert(2,str(os.path.dirname(my_filename)))
            # print(str("the dir is" + os.path.dirname(os.path.dirname(os.path.basename(my_path)))))
            print(str("the dir is " + os.path.split(os.path.split(my_path)[0])[1]))
            row.insert(2,os.path.split(os.path.split(my_path)[0])[1])
            row.insert(2,str(my_filename))
            writer.writerow(row)

print ('process is complete')  
    
              