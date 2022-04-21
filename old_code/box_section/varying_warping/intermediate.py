import sys

d=float(sys.argv[1])

file = open(r"E:\temp\box\d.txt", "w")
file.write(str(d))
file.close()

