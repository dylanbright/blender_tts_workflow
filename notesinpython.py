import bpy
import os

# Modifying Object Origin

# https://blenderartists.org/t/modifying-object-origin-with-python/507305/2

# store the location of current 3d cursor
saved_location = bpy.context.scene.cursor_location  # returns a vector

# give 3dcursor new coordinates
bpy.context.scene.cursor_location = Vector((1.0,0.0,0.0))

# set the origin on the current object to the 3dcursor location
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

# set 3dcursor location back to the stored location
bpy.context.scene.cursor_location = saved_location

# Decimate the object from https://gist.github.com/wooddar/0a5f409dc67cc045c421

# change the below value to choose how many frames the effect will be iterated over
numberOfFrames = 15

# starting value of the Decimate ratio [must be <= 1].
startRatio = 1

# Final ratio value desired
finalRatio = 0.0001

# Iteration value is calculated here
iterationValue = (finalRatio / startRatio) ** (1 / numberOfFrames)

for i in range(numberOfFrames):
    bpy.ops.object.modifier_add(type='DECIMATE')
    bpy.context.object.modifiers["Decimate"].use_collapse_triangulate = True

    bpy.context.object.modifiers["Decimate"].ratio = startRatio * (iterationValue ** i)

    # fill in the filepath below, frames will be numbered consecutively
    bpy.data.scenes['Scene'].render.filepath = 'C:\\...................................\\Frame-%d.png' % i
    bpy.ops.render.render(write_still=True)



# Exporting object

blend_file_path = bpy.data.filepath
directory = os.path.dirname(blend_file_path)
bpy.ops.export_scene.obj(filepath="", check_existing=True, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=False, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1, path_mode='AUTO')
target_file = os.path.join(directory, 'myfile.obj')

bpy.ops.export_scene.obj(filepath=target_file)