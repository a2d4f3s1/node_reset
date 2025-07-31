import bpy

class NODE_OT_reset_node_positions(bpy.types.Operator):
    """すべてのノードの座標をリセット"""
    bl_idname = "node.reset_node_positions"
    bl_label = "ノード位置リセット"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # アクティブなノードエディターのノードツリーを取得
        node_tree = context.space_data.edit_tree  # これでアクティブなノードツリーを取得
        
        if not node_tree:
            self.report({'WARNING'}, "コンポジターのノードツリーがありません")
            return {'CANCELLED'}
        
        selected_nodes = [node for node in node_tree.nodes if node.select]
        
        if not selected_nodes:
            self.report({'WARNING'}, "選択されたノードがありません")
            return {'CANCELLED'}
        
        for node in selected_nodes:
            node.location = (0, 0)
        
        self.report({'INFO'}, f"{len(selected_nodes)} 個のノード位置をリセットしました")
        return {'FINISHED'}

# 登録・解除関数
classes = [NODE_OT_reset_node_positions]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
