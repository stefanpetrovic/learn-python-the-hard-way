try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup


config = {
	'description': 'My project',
	'author' : 'Stefan Petrovic',
 	'url' : '',
 	'download_url' : '',
 	'author_email' : 'petrovicstefan91@gmail.com',
 	'version' : '1.0',
 	'install_requires' : ['nose'],
 	'packages' : ['NAME'],
 	'scripts' : [],
 	'name' : 'projectname'
}

setup(**config)