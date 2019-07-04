import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
	name="distros-jl7",
	version="1.0.0",
	author="José Luís",
	author_email="zeluis0712@gmail.com",
	description="A small example, how to organize python project",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/JL07/Estrutura-de-Projecto-Python",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3 :: 2"

	]
)