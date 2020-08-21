from os import listdir
import csv

'''
Reads the contents of a CSV file containing a series of image filenames
and writes a new CSV file with a path added to the filenames 

date: August 06 2020
'''

# edit these variables
my_image_folder = "2020-07-15-Camera1"
training_run = "training-run-8/"

# do not edit these variables
my_csv = "output-" + my_image_folder + ".csv"
my_edited_csv = "output-" + my_image_folder + "-edited.csv"
my_image_path = "D:/non-dropbox-files/research/looking-at-animals-captured-images/" + my_image_folder + "/"
my_csv_path = "D:/non-dropbox-files/research/looking-at-animals-training-runs/"


print(my_csv_path + training_run + "my-data/" + my_csv)
lines = []
# with open(my_csv_path + training_run + "my-data/" + my_csv, "r") as csvfile:
with open(my_csv_path + training_run + "my-data/" + my_csv, "r") as infile, open(my_csv_path + training_run + "my-data/" + my_edited_csv, "w", newline='') as outfile:
    readCSV = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(readCSV)
    if header != None:
        writer.writerow(header)
    #  next(readCSV, None)  # skip the headers
    
    my_count = 0
    for row in readCSV:
        row[1] = my_image_path + row[1]
        # row = row.rstrip(',\n') + '\n'
        print(row)
        writer.writerow(row)
        #lines[my_count] = row
        my_count = my_count + 1

		
print ('process is complete')  
    
              