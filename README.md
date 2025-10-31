# Blender-Viewport-Visibility-to-Render
Apply the visibility animation to render if you only have the viewport keyframes 

### How To Use
1. Click and open the "viewport_visibility_to_render.py" file
2. Copy all the code
3. Open Blender and click "Scripting" on the top bar
4. Click "+ New" at the top of the middle window.
5. Paste the code
6. Click the "Run Code" near to the "X"
7. Done!

### image-based instructions
1. Click this file and copy all the code inside
<img width="331" alt="1" src="https://github.com/user-attachments/assets/0510420e-4191-40c5-9687-83244694c18a">

2. Open Blender and click "Scripting" on the top bar
<img width="1116" alt="2" src="https://github.com/user-attachments/assets/dec18927-6858-4460-aa17-9d20a38c3c62">

3. Click "+ New" and paste the code below
<img width="1332" alt="3" src="https://github.com/user-attachments/assets/e771df7c-8460-4e5b-973a-4c07f1ecd4e4">

4. Run the code, and you're done!
<img width="1380" alt="4" src="https://github.com/user-attachments/assets/caced066-7381-45d7-ab87-9c857229fb66">

#### Just in case
code is here
```
import bpy

scene = bpy.context.scene
start_frame = scene.frame_start
end_frame = scene.frame_end

#detect if the object is visible when animation starts
for frame in range (start_frame - 1, start_frame):
    for obj in scene.objects:
         if obj.hide_viewport:
                obj.hide_render = True
         else:
                obj.hide_render = False
         obj.keyframe_insert(data_path="hide_render", frame=frame)
        

#loop each frame
for frame in range(start_frame-1, end_frame + 1):
    scene.frame_set(frame)
    
    #see if there's an animation keyframe
    for obj in scene.objects:
        if obj.animation_data and obj.animation_data.action:
            current_hide_render = obj.hide_render
            current_hide_viewport = obj.hide_viewport
            
            # if it's invisible in viewport, hide in render
            if current_hide_viewport:
                obj.hide_render = True
            else:
                obj.hide_render = False
            
            # insert keyframe only if the visibility status changed
            if obj.hide_render != current_hide_render:
                obj.keyframe_insert(data_path="hide_render", frame=frame)

# update the scene after code finish running
bpy.context.view_layer.update()
```




# Demo on Youtube
[![Watch on YouTube](https://img.youtube.com/vi/5D47lvzuFEQ/0.jpg)](https://www.youtube.com/watch?v=5D47lvzuFEQ)


