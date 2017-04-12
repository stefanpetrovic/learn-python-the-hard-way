formatter = '%r %r %r %r'

print formatter % (1, 2, 3, 4)
print formatter % (formatter, formatter, formatter, formatter)

print formatter % ("long string  adadsadadsa  dsadsadsadsa", "long string 2", "long string 3", "long string 4")