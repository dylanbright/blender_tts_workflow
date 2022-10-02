import os

full_path_to_directory = os.path.join('E:\\', 'TTS_Mini_Factory', 'blender_queue')

# get list of all files in directory
file_list = os.listdir(full_path_to_directory)

# reduce the list to files ending in 'obj'
# using 'list comprehensions'
obj_list = [item for item in file_list if item[-3:] == 'obj']
full_path_to_file = os.path.join(full_path_to_directory, obj_list)
