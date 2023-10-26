# setup.py
# This script is used for building the executable of the file
import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use this for Windows GUI applications

setup(
    name="new_encrypt",
    version="0.1",
    description="This will encrypt your information",
    executables=[Executable("new_encrypt.py", base=base)]
)
