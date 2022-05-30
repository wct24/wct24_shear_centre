import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

input_string = r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.02_5.0\\210.0_81.0_0.3\\Warping"

#there are 6 part to any beam name
x = input_string.split( r"\\"  )

print(x)
assert len(x)==6, r"The name of the beam need to be a raw string and directory address is spaced with \\ "
print(int(str(x[2])[0]))




material = list(np.float_(x[3].split( r"_" )))
print(material)
