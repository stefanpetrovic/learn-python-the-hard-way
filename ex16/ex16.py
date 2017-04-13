from sys import argv

script, filename = argv

print 'deleting file: %s ' % filename

file = open(filename, 'w')

file.truncate()

print 'deleted file'

firstln = raw_input("first line")
secondln = raw_input("second line")
thirdln = raw_input("third line")

file.write(firstln)
file.write("\n")

file.write(secondln)
file.write("\n")

file.write(thirdln)

file.close()

print 'closed file'
