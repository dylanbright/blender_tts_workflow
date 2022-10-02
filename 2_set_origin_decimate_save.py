# Part 2 of Blender workflow.  Sets the origin, decimates the object to TTS levels, and saves it.
import bpy
import os
import shutil


def main(context):
    for ob in context.scene.objects:
        print(ob)


class set_origin_decimate_save_for_tts(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.set_origin_decimate_save_for_tts"
    bl_label = "2.set_origin_decimate_save_for_tts"

    def execute(self, context):
        # Modifying Object Origin
        # https://blenderartists.org/t/modifying-object-origin-with-python/507305/2
        # store the location of current 3d cursor
        #        saved_location = bpy.data.scenes[0].cursor.location

        # give 3dcursor new coordinates
        # bpy.data.scenes[0].cursor.location = Vector((0.0, 0.0, 0.0))

        # set the origin on the current object to the 3dcursor location
        bpy.data.objects[0].select_set(True)  # make sure the object is selected.
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

        #        # set 3dcursor location back to the stored location
        #        bpy.context.scene.cursor_location = saved_location
        print('set origin to 3d cursor')

        # Decimate the object
        starting_polygons = len(bpy.context.object.data.polygons)
        print('starting polygons: ', starting_polygons)
        # if there are more than 16000 then decimate.
        if (starting_polygons > 16000):
            print('more than 16000, will decimate')
            # Find the ratio we need to get to 16K polygons
            decimate_ratio = 16000 / starting_polygons
            print('more than 16000, will decimate with ratio: ', decimate_ratio)
            bpy.ops.object.modifier_add(type='DECIMATE')
            bpy.context.object.modifiers["Decimate"].use_collapse_triangulate = True
            bpy.context.object.modifiers["Decimate"].ratio = decimate_ratio
            bpy.ops.object.modifier_apply(modifier="Decimate")
            print('New polygons: ', len(bpy.context.object.data.polygons))

        # Export the obj for TTS.

        blend_file_path = os.path.join('E:\\', 'TTS_Mini_Factory', 'post_blender_obj')
        blend_file_name = bpy.context.object.name.split(".")[0] + "_blend.obj"
        blend_file_full_path = os.path.join(blend_file_path, blend_file_name)
        print('Saving file to: ', blend_file_full_path)
        bpy.ops.export_scene.obj(filepath=blend_file_full_path, check_existing=True, axis_forward='Z', axis_up='Y',
                                 filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False,
                                 use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False,
                                 use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True,
                                 use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True,
                                 group_by_object=False, group_by_material=False, keep_vertex_order=False,
                                 global_scale=1, path_mode='AUTO')
        print('Save file complete.')
        # Copy the texture jpg
        print('Copying Texture file.')
        source_jpg_file_name = blend_file_name.replace("_blend.obj", ".jpg")
        source_jpg_file_path = os.path.join('e:\\', 'TTS_Mini_Factory', 'blender_queue', source_jpg_file_name)
        destination_file_path = os.path.join(blend_file_path, source_jpg_file_name)
        shutil.copyfile(source_jpg_file_path, destination_file_path)
        print('Texture coped to: ', destination_file_path)
        # prepend COMPLETE_ to the orginal files.
        full_path_to_directory = os.path.join('E:\\', 'TTS_Mini_Factory', 'blender_queue')
        file_list = os.listdir(full_path_to_directory)
        file_name_prefix = bpy.context.object.name.split(".")[0]
        filtered_list = list(filter(lambda k: file_name_prefix in k, file_list))
        #  TO DO:  ADD FILE RENAME PART
        for item in filtered_list:
            src_path = os.path.join('E:\\', 'TTS_Mini_Factory', 'blender_queue', item)
            new_name = "processed_" + item
            dst_path = os.path.join('E:\\', 'TTS_Mini_Factory', 'blender_queue', new_name)
            os.rename(src=src_path, dst=dst_path)
            print('renamed: ', src_path, ' to: ', dst_path)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(set_origin_decimate_save_for_tts)


def unregister():
    bpy.utils.unregister_class(set_origin_decimate_save_for_tts)


if __name__ == "__main__":
    register()

    # test call
