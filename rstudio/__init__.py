import sublime
import os
from ..applescript import execute_applescript
from ..autohotkey import execute_autohotkey_script
from ..clipboard import Clipboard

RSTUDIOAPPLESCRIPT = os.path.join(os.path.dirname(__file__), "rstudio.applescript")
RSTUDIOAHK = os.path.join(os.path.dirname(__file__), "rstudio.ahk")


plat = sublime.platform()

if plat == "osx":
    def send_to_rstudio(cmd):
        execute_applescript(RSTUDIOAPPLESCRIPT, cmd)

elif plat == "windows":
    def send_to_rstudio(cmd):
        Clipboard.set_clipboard(cmd)
        execute_autohotkey_script(RSTUDIOAHK)
        Clipboard.reset_clipboard()

elif plat == "linux":
    def send_to_rstudio(cmd):
        pass
