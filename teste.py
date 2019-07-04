from  distros import Rpm  
from  distros import Deb    

def main(args):
	rpm = Rpm()
	rpm.show_distros()
	deb = Deb()
	deb.show_distros()

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))