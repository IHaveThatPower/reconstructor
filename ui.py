from bpy.types import Panel
import bmesh, bpy

# from . import report

class ViewReconstructorPanel:
	bl_category = "Reconstructor"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'

	@classmethod
	def poll(cls, context):
		# obj = context.active_object
		return True # obj is not None and obj.type == 'MESH' and obj.mode in {'OBJECT', 'EDIT'}

class VIEW3D_PT_reconstructor_cameras(ViewReconstructorPanel, Panel):
	bl_label = "1. Cameras"

	def draw(self, context):
		layout = self.layout

		reconstructor = context.scene.reconstructor

		# Clips section
		clips = bpy.data.movieclips
		layout.label(text="Clips")
		row = layout.row(align=True)
		row.label(text="Clip")
		row.label(text="Camera")
		row.label(text="Use")
		for clip in clips:
			row = layout.row(align=True)
			row.prop(clip, "name", text="")
			row.enabled = False
			row.label(text="Camera?")
			# row.prop(reconstructor.clip_cameras, "clip[%s]" % clip.id, text="")
			# row.prop(reconstructor.clip_active, "clip[%s]" % clip.id, text="")
			# row.menu("camera_menu", text="Camera?")
		"""
		row.operator("mesh.print3d_info_volume", text="Volume")
		row.operator("mesh.print3d_info_area", text="Area")

		layout.label(text="Checks")
		col = layout.column(align=True)
		col.operator("mesh.print3d_check_solid", text="Solid")
		col.operator("mesh.print3d_check_intersect", text="Intersections")
		row = col.row(align=True)
		row.operator("mesh.print3d_check_degenerate", text="Degenerate")
		row.prop(reconstructor, "threshold_zero", text="")
		row = col.row(align=True)
		row.operator("mesh.print3d_check_distort", text="Distorted")
		row.prop(reconstructor, "angle_distort", text="")
		row = col.row(align=True)
		row.operator("mesh.print3d_check_thick", text="Thickness")
		row.prop(reconstructor, "thickness_min", text="")
		row = col.row(align=True)
		row.operator("mesh.print3d_check_sharp", text="Edge Sharp")
		row.prop(reconstructor, "angle_sharp", text="")
		row = col.row(align=True)
		row.operator("mesh.print3d_check_overhang", text="Overhang")
		row.prop(reconstructor, "angle_overhang", text="")
		layout.operator("mesh.print3d_check_all", text="Check All")
		"""

		# self.draw_report(context)

class VIEW3D_PT_reconstructor_empties(ViewReconstructorPanel, Panel):
	bl_label = "2. Create/Update Empties"

	def draw(self, context):
		layout = self.layout

class VIEW3D_PT_reconstructor_empty_links(ViewReconstructorPanel, Panel):
	bl_label = "3. Link Empties"
	
	def draw(self, context):
		layout = self.layout

class VIEW3D_PT_reconstructor_tolerance(ViewReconstructorPanel, Panel):
	bl_label = "4. Tolerance"
	
	def draw(self, context):
		layout = self.layout

class VIEW3D_PT_reconstructor_solve(ViewReconstructorPanel, Panel):
	bl_label = "5. Solve"
	
	def draw(self, context):
		layout = self.layout