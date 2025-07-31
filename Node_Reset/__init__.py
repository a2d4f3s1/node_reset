bl_info = {
    "name": "Node Reset",
    "author": "Moteki",
    "version": (0, 0, 1),
    "blender": (3, 3, 0),
    "location": "Node Editor > N Panel",
    "description": "ノードを[0,0]にリセットする",
    "category": "Node",
}

import bpy
from . import operators, panel  # 必要なモジュールをインポート

def register():
    operators.register()
    panel.register()

def unregister():
    panel.unregister()
    operators.unregister()

if __name__ == "__main__":
    register()