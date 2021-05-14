import bpy
import sys
import addon_utils
from pathlib import Path

def get_python_path():
    if bpy.app.version < (2,9,0):
        python_path = bpy.app.binary_path_python
    else:
        python_path = sys.executable
    return Path(python_path)

python_path = get_python_path()
blender_path = Path(bpy.app.binary_path)
blender_directory = blender_path.parent
use_own_python = blender_directory in python_path.parents

version = bpy.app.version
scripts_folder = blender_path.parent / f"{version[0]}.{version[1]}" / "scripts"
user_addon_directory = Path(bpy.utils.user_resource('SCRIPTS', "addons"))
addon_directories = tuple(map(Path, addon_utils.paths()))
