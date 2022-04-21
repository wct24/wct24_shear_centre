import sys
beam_number=float(sys.argv[1])

file = open(r"C:\Users\touze\project\Shear_centre\I-beam\beam_number.txt", "w")
file.write(str(beam_number))
file.close()

