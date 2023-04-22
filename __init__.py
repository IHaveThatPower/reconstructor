bl_info = {
	"name": "Reconstructor",
	"author": "Ryan McClure",
	"blender": (3, 5, 0),
	"location": "3D View > Sidebar",
	"description": "Utility for landmark-based camera reconstruction",
	"category": "3D View",
}

if "bpy" in locals():
	import importlib
	importlib.reload(ui)
	# importlib.reload(operators)
	# if "mesh_helpers" in locals():
	#     importlib.reload(mesh_helpers)
	# if "export" in locals():
	#     importlib.reload(export)
else:
	import math

	import bpy
	from bpy.types import PropertyGroup
	from bpy.props import (
		StringProperty,
		BoolProperty,
		FloatProperty,
		EnumProperty,
		PointerProperty,
	)

	from . import (
		ui,
	#    operators,
	)

class SceneProperties(PropertyGroup):
	use_alignxy_face_area: BoolProperty(
		name="Face Areas",
		description="Normalize normals proportional to face areas",
		default=False,
	)

classes = (
	SceneProperties,

	ui.VIEW3D_PT_reconstructor_cameras,
	ui.VIEW3D_PT_reconstructor_empties,
	ui.VIEW3D_PT_reconstructor_empty_links,
	ui.VIEW3D_PT_reconstructor_tolerance,
	ui.VIEW3D_PT_reconstructor_solve,
)
"""
ui.VIEW3D_PT_print3d_cleanup,
ui.VIEW3D_PT_print3d_transform,
ui.VIEW3D_PT_print3d_export,

operators.MESH_OT_print3d_info_volume,
operators.MESH_OT_print3d_info_area,
operators.MESH_OT_print3d_check_degenerate,
operators.MESH_OT_print3d_check_distorted,
operators.MESH_OT_print3d_check_solid,
operators.MESH_OT_print3d_check_intersections,
operators.MESH_OT_print3d_check_thick,
operators.MESH_OT_print3d_check_sharp,
operators.MESH_OT_print3d_check_overhang,
operators.MESH_OT_print3d_check_all,
operators.MESH_OT_print3d_clean_distorted,
# operators.MESH_OT_print3d_clean_thin,
operators.MESH_OT_print3d_clean_non_manifold,
operators.MESH_OT_print3d_select_report,
operators.MESH_OT_print3d_scale_to_volume,
operators.MESH_OT_print3d_scale_to_bounds,
operators.MESH_OT_print3d_align_to_xy,
operators.MESH_OT_print3d_export,
"""

def register():
	for cls in classes:
		 bpy.utils.register_class(cls) 
	bpy.types.Scene.reconstructor = PointerProperty(type=SceneProperties)


def unregister():
	for cls in classes:
		 bpy.utils.unregister_class(cls)
	del bpy.types.Scene.reconstructor