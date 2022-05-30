import pandas as pd
import os
import matplotlib.pyplot as plt

beam_number = 0

df = pd.read_csv("input.csv", header = 0, index_col = 0)
print(df)

def TSC(bn):
    dim = str(df['Dimensions'][beam_number])
    dim = dim.replace(", ", "_")
    dim = dim.replace("[", "")
    dim = dim.replace("]", "")
    folder_name = r"E:\shear_centre\{}\{}\{}\{}".format(str(df['ShapeName'][beam_number]),dim, "TSC",str(df['LoadingPosition'][beam_number]))

    isExist = os.path.exists(folder_name)
    if not isExist:
        os.makedirs(folder_name)
    os.chdir(folder_name)
    single_beam_data_frame = df.iloc[[0]]
    print(single_beam_data_frame)
    single_beam_data_frame["LoadingX"] = [-10.0]
    single_beam_data_frame.to_csv('beam.csv')






if df["AnalysisType"][beam_number] == 1:
    TSC(beam_number)

