import os
import glob

my_image_directory = "2020-07-15-Camera1"
my_image_path = "D:/non-dropbox-files/research/looking-at-animals-captured-images/" + my_image_directory + "/"
my_training_path = "D:/non-dropbox-files/research/looking-at-animals-training-data/training-data-"

paths = glob.glob(my_image_path + '/**/*.JPG', recursive=True)
# files = [os.path.basename(x) for x in paths]



with open(my_training_path + my_image_directory + "/output-" + my_image_directory + ".txt", "w+") as a:
    a.write("ID, path, image, species, count" + "\n")
    IDCount = 1
    for my_path in paths:
        my_file = os.path.basename(my_path)
        a.write(str(IDCount) + "," + str(my_path) + "," + my_file + ",," + "\n")
        print(my_file)
        IDCount +=1

print("process is complete")
