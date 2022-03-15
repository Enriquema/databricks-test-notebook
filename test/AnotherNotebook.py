import sys

var1=sys.argv[1]
var2=sys.argv[2]

outF = open("myOutFile.txt", "w")
print("writing "+var1+" "+var2)
outF.writelines(var1+" "+var2)
outF.close()
