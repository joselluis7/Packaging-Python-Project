#This is the first module to be executed 
#And Transform the current dir in package
name = "distros"

from .rpm import Rpm
from .deb import Deb
