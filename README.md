# Reconstructor
Camera position reconstructor for Blender, using correlated motion tracker markers across different movie clips to solve camera positions

## General Plan/Workflow
1. Create motion tracks from clips with matching focal lengths.
	* Individual images within clips must have the same focal length
	* Clips should be at least partially track-solved (if correspondences found) to derive optical center or distortion params.
2. ADDON: Create cameras for each clip.
	* Alternately, can link clips to existing cameras.
	* Define rough axial position wrt target object (i.e. front, above, left) to prime/constrain solve
	* Crux: cameras correlate with clips.
3. ADDON: Create empties for each tracked element.
	* https://blender.stackexchange.com/questions/248078/how-can-i-get-the-list-of-all-tracking-markers-using-python-command
4. ADDON: Associate correlated empties from different clips, so that their "solves" can converge
5. ADDON: Solve -> Bundle adjust linked empties and cameras to minimize distance between linked empties
	* Beware converging the cameras toward 0
6. RESULT: Cameras and empties positioned in best approximation of analogous 3D positions, with minimized error
