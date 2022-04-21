import sys
sc=float(sys.argv[1])
loading_z = float(sys.argv[2])

file = open(r"E:\temp\NACA0025\sample.txt", "w")
file.write(str(sc))
file.close()

file = open(r"E:\temp\NACA0025\loading_z.txt", "w")
file.write(str(loading_z))
file.close()

