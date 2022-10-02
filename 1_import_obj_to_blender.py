# Part 1 of Blender workflow.  Imports the object.
import bpy
import os


def main(context):
    for ob in context.scene.objects:
        print(ob)


class import_for_tts_operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.import_obj_for_tts"
    bl_label = "1.Import Obj for TTS"

    def execute(self, context):
        # Directory where we store files to process
        full_path_to_directory = os.path.join('E:\\', 'TTS_Mini_Factory', 'blender_queue')

        # get list of all files in directory
        file_list = os.listdir(full_path_to_directory)

        # reduce the list to files ending in 'obj'
        # using 'list comprehensions'
        obj_list = [item for item in file_list if item[-3:] == 'obj' and item[0:10] != "processed_"]
        # get the full path to the first file
        full_path_to_file = os.path.join(full_path_to_directory, obj_list[0])
        # Import the object so it is right side up.
        imported_object = bpy.ops.import_scene.obj(filepath=full_path_to_file, axis_forward='-X', axis_up='Z')
        obj_object = bpy.context.selected_objects[0]
        print('Imported name: ', obj_object.name)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(import_for_tts_operator)


def unregister():
    bpy.utils.unregister_class(import_for_tts_operator)


if __name__ == "__main__":
    register()

# don't forget to go into prefereneces and enable developer extras so it shows in the F3 menu.
