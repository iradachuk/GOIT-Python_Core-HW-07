from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0',
    description='Clean folder script',
    url='https://github.com/iradachuk/GOIT-Python_Core-HW-07',
    author='Iryna Dachuk',
    author_email='iradachuk@gmail.com',
    packages=find_namespace_packages(),
    long_description=open('README.md').read(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.sort:run']}
    )
    