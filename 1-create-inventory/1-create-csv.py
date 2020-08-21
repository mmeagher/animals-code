from os import listdir

my_image_directory = "2020-07-09-Camera3"
my_image_path = "D:/non-dropbox-files/research/looking-at-animals-captured-images/" + my_image_directory + "/"
my_training_path = "D:/non-dropbox-files/research/looking-at-animals-training-data/training-data-"

with open(my_training_path + my_image_directory + "/output-" + my_image_directory + ".txt", "w+") as a:
    a.write("ID, image, species, count" + "\n")
    IDCount = 1
    for files in listdir(my_image_path):
        a.write(str(IDCount) + "," + str(files) + ",," + "\n") 
        IDCount +=1            