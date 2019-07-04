#-*-coding:utf-8-*-
class Deb():
	def __init__(self):
		self.distro_list = ["Debian","Ubuntu","Mint"]
	def show_distros(self):
		print("Distribuições Debian: ")
		for distro in self.distro_list:
			print("\t%s"%distro)