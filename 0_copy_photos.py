from shutil import copyfile
import os
# this script copied files to the places where I need them.
# run from pycharm or however you like to run python on your computer.

target_path = os.path.join('E:\\', 'TTS_Mini_Factory', 'photo_queue')


def create_find_next_folder(target_path):
    dir_contents = list(map(int, (os.listdir(target_path))))
    next_dir_name = max(dir_contents) + 1
    print('new dir name: ', next_dir_name)
    new_dir_path = os.path.join(target_path, str(next_dir_name))
    os.mkdir(new_dir_path)
    return new_dir_path


def copy_photos(drive_letter):
    # copy files from the SD card to a place.

    # prompt user for starting file.
    file_offset = int(input("Number of photos to skip: "))
    # F:\DCIM\101D5600
    source_directory = os.path.join(drive_letter + ':\\', 'DCIM', '101D5600')
    print(f'We will skip {file_offset} photos in {source_directory}')

    # iterate the list of files.
    file_list = os.listdir(source_directory)
    photos_counter = 0
    current_folder = create_find_next_folder(target_path)
    print(f'created first folder: {current_folder}')
    for index, file in enumerate(file_list, start=1):
        photos_counter = photos_counter + 1
        if index > (file_offset - 1):
            if photos_counter < 51:
                print(index, file)
                source = os.path.join(source_directory, file)
                destination = os.path.join(current_folder, file)
                copyfile(source, destination)
            else:
                print('Creating new folder...')
                try:
                    current_folder = create_find_next_folder(target_path)
                except BaseException:
                    print('could not create folder!')
                    raise BaseException
                    exit(1)
                print(index, file)
                source = os.path.join(source_directory, file)
                destination = os.path.join(current_folder, file)
                copyfile(source, destination)
                photos_counter = 1
    # for group of 50 create a folder.

    # Copy the 50 files.

if __name__ == '__main__':
    copy_photos("F")  # Drive letter of the SD card.
