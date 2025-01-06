import sys

fileOpend = open('FileHandling\\WeWillprint.txt', 'w')

print("File is open", file=fileOpend)
print("We are using print function", file=fileOpend, end='')
print("This will be printed", file=sys.stderr)

fileOpend.close()
