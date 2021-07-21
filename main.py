import ctypes
import os.path

dir_path = os.path.dirname(os.path.realpath(__file__))+"\\"+"wall.jpg"

ctypes.windll.user32.SystemParametersInfoW(20,0,dir_path, 0) 