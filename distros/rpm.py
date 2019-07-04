#-*-coding:utf-8-*-
class Rpm():
	
	def __init__(self):
		self.distro_list = ["Red-Hat","Centos","Fedora" ]

	def show_distros(self):
		print("RPM Distros:")
		for distro in self.distro_list:
			print("\t%s "% distro)

