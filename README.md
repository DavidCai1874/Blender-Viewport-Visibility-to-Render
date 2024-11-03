# Blender-Viewport-Visibility-to-Render
Apply the visibility animation to render if you only have the viewport keyframes / 把3D视图的可见性动画帧插入到渲染

### How To Use
1. Click and open the "viewport_visibility_to_render.py" file
2. Copy all the code
3. Open Blender and click "Scripting" on the top bar
4. Click "+ New" at the top of the middle window.
5. Paste the code
6. Click the "Run Code" near to the "X"
7. Done!

### 用法
1. 点击打开 "viewport_visibility_to_render.py" 文件
2. 复制所有的代码
3. 打开Blender,点击最上面一栏的"Scripting"
4. 点击中间窗口最上面的 "+ New"
5. 粘贴代码
6. 点击运行键, 在顶栏"x"的旁边
7. 完成!

### image-based instructions/图片版教程
1. Click this file and copy all the code inside / 点击这个文件,并且全选,复制文件内所有代码
<img width="331" alt="1" src="https://github.com/user-attachments/assets/0510420e-4191-40c5-9687-83244694c18a">

2. Open Blender and click "Scripting" on the top bar / 打开Blender, 点击上方的scripting
<img width="1116" alt="2" src="https://github.com/user-attachments/assets/dec18927-6858-4460-aa17-9d20a38c3c62">

3. Click "+ New" and paste the code below / 进入后点击页面上方的"+New", 并且在下方粘贴代码
<img width="1332" alt="3" src="https://github.com/user-attachments/assets/e771df7c-8460-4e5b-973a-4c07f1ecd4e4">

4. Run the code, and you're done! / 点击运行,完成!
<img width="1380" alt="4" src="https://github.com/user-attachments/assets/caced066-7381-45d7-ab87-9c857229fb66">

#### Just in case
code is here
```
import bpy

scene = bpy.context.scene
start_frame = scene.frame_start
end_frame = scene.frame_end

#detect if the object is visible when animation starts/检测在动画开始时物体是否可见
for frame in range (start_frame - 1, start_frame):
    for obj in scene.objects:
         if obj.hide_viewport:
                obj.hide_render = True
         else:
                obj.hide_render = False
         obj.keyframe_insert(data_path="hide_render", frame=frame)
        

#loop each frame/遍历每一帧
for frame in range(start_frame-1, end_frame + 1):
    scene.frame_set(frame)
    
    #see if there's an animation keyframe/检测是否有关键帧
    for obj in scene.objects:
        if obj.animation_data and obj.animation_data.action:
            current_hide_render = obj.hide_render
            current_hide_viewport = obj.hide_viewport
            
            # if it's invisible in viewport, hide in render/要是视图中不可见,则让渲染也不可见
            if current_hide_viewport:
                obj.hide_render = True
            else:
                obj.hide_render = False
            
            # insert keyframe only if the visibility status changed/要是出现或者消失了, 则打上关键帧
            if obj.hide_render != current_hide_render:
                obj.keyframe_insert(data_path="hide_render", frame=frame)

# update the scene after code finish running/运行完代码后更新场景
bpy.context.view_layer.update()
```




# YouTube Demo
[![Watch on YouTube](https://img.youtube.com/vi/5D47lvzuFEQ/0.jpg)](https://www.youtube.com/watch?v=5D47lvzuFEQ)


