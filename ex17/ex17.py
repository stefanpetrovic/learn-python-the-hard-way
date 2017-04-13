from sys import argv
from os.path import exists

script, from_file, to_file = argv

original_file = open(from_file)
content = original_file.read()

file_copy = open(to_file, 'w')

file_copy.write("Copy of the %s \n" % from_file)
file_copy.write(content)

file_copy.close()
original_file.close()

print 'copied files'
