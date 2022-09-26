import os

images_in_file = []
path_to_imgs = 'C:\\Users\\john_\\MSc Comp Sci\\Semester 1\\Software engineering\\DungeonGame\\Images\\Character'

for filename in os.listdir(path_to_imgs):
    if filename.endswith(".png"):
        # add each image paths into an array, so each images path acts like a variable corresponding to array elements
         images_in_file.append( os.getcwd() + '\\' + filename)
    else:
        continue

# check that they're properly stored in array
for element in images_in_file:
    print(element)