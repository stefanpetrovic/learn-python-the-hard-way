from sys import argv

script, filename = argv

txt = open(filename)

print 'file content %s' % txt.read()

txt.close()

print 'closed file'
