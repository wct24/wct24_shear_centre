import sys
sc=float(sys.argv[1])
loading_z = float(sys.argv[2])

file = open(r"E:\temp\reid_section\sample.txt", "w")
file.write(str(sc))
file.close()

file = open(r"E:\temp\reid_section\loading_z.txt", "w")
file.write(str(loading_z))
file.close()

