filename = "file1.txt"
filedata = open(filename, 'w')
#filedata.truncate()

filedata.write("Writing in files; ")
filedata.write("\nWriting in files1; ")
# filedata.close()
# filedata = open(filename, 'r')
#
# print "All line individally"
# print filedata.readline()
# print filedata.readline()
# print filedata.readline()
#
# filedata = open(filename, 'r')
# print "All line together"
# print filedata.read()

filedata = open(filename, 'r')
print filedata.readline()
filedata.seek(0)
print filedata.readline()
print filedata.readline()
filedata.seek(0)
print filedata.readline()
# same way u can copy file from one to another.
