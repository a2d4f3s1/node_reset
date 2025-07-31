import bpy
from .operators import NODE_OT_reset_node_positions  # オペレーターをインポート

class NODE_PT_custom_panel(bpy.types.Panel):
    bl_label = "Node Reset"
    bl_idname = "NODE_PT_custom_panel"
    bl_space_type = 'NODE_EDITOR'  # ノードエディター
    bl_region_type = 'UI'           # Nパネル
    bl_category = "Node Relax"        # タブの名前
    bl_context = "node"             # ノード用のパネル

    def draw(self, context):
        layout = self.layout
        layout.label(text="ノードツール")
        layout.operator("node.reset_node_positions", text="ノード位置リセット")

# 登録・解除関数
classes = [NODE_PT_custom_panel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
