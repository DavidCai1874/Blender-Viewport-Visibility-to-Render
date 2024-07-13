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