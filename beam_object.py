import subprocess
import smtplib, ssl
import pandas as pd
import os
import time
import numpy as np
from transforms3d.euler import mat2euler
import math
import matplotlib.pyplot as plt

from decimal import Decimal

# class AnalysisMethod:
#     def __init__(self):
#         pass

#     def create_folder(self):

class Result_Data:
    def __init__(self, beam_csv, output_csv_displacement, output_csv_stress):
        self.beam_csv = beam_csv
        self.beam_df = pd.read_csv(self.beam_csv, header = 0,index_col=0)
        self.output_csv_displacement = output_csv_displacement
        self.output_csv_stress = output_csv_stress
        self.U_df = self._displacement_csv_to_data_frame(self.output_csv_displacement)
        self.list_of_z_values = np.flip(np.unique(self.U_df["z"].values))

    def _displacement_csv_to_data_frame(self, csv_filename):
        u = pd.read_csv(csv_filename, header = 0, usecols = [3, 12,13,14,16,17,18])
        u.columns=["Part Instance", "x", "y", "z","U1", "U2", "U3" ]
        NoValue = "ASSEMBLY"  ## remove the loading point
        indexNames = u[u["Part Instance"]==NoValue].index
        u.drop(indexNames , inplace=True)
        u.drop(labels = "Part Instance", axis=1, inplace = True)
        u = u.astype(np.float64)
        return u
    def section_rotationz(self, ResultSection):
        ''''takes a z coordinate and an abaqus output file directory and returns the axial rotation'''
        z = self.list_of_z_values[ResultSection]
        df2 = self.U_df.loc[self.U_df["z"]==z]
        x_0 = df2["x"].values
        y_0 = df2["y"].values
        z_0 = df2["z"].values
        AF =1
        x_1 = x_0 + df2["U1"].values*AF
        y_1 = y_0 + df2["U2"].values*AF
        z_1 = z_0 + df2["U3"].values*AF
        A = np.vstack([x_1,y_1,z_1])
        B = np.vstack([x_0,y_0,z_0])

        assert A.shape == B.shape

        num_rows, num_cols = A.shape
        if num_rows != 3:
            raise Exception(f"matrix A is not 3xN, it is {num_rows}x{num_cols}")

        num_rows, num_cols = B.shape
        if num_rows != 3:
            raise Exception(f"matrix B is not 3xN, it is {num_rows}x{num_cols}")

        # find mean column wise
        centroid_A = np.mean(A, axis=1)
        centroid_B = np.mean(B, axis=1)

        # ensure centroids are 3x1
        centroid_A = centroid_A.reshape(-1, 1)
        centroid_B = centroid_B.reshape(-1, 1)

        # subtract mean
        Am = A - centroid_A
        Bm = B - centroid_B

        H = Am @ np.transpose(Bm)

        # find rotation
        U, S, Vt = np.linalg.svd(H)
        R = Vt.T @ U.T


        t = -R @ centroid_A + centroid_B
        XYZ_2  = R @ A + t


        x_2 = XYZ_2[0]
        y_2 = XYZ_2[1]
        z_2 = XYZ_2[2]

        # plt.scatter(x_0, y_0)
        # plt.scatter(x_2, y_2)
        # plt.gca().set_aspect('equal', adjustable='box')
        ang = mat2euler(R, axes='sxyz')
        # e = np.sqrt(np.sum((x_2-x_0)**2)+np.sum((y_2-y_0)**2)+np.sum((z_2-z_0)**2))
        return ang[2]

    def plot_z_rotation_along_beam(self):

        rotation_z_list =[]
        for i in range(len(self.list_of_z_values)):
            rotation_z_list.append(self.section_rotationz(i)*180/np.pi)
        z_list = self.list_of_z_values
        ax.plot(z_list, rotation_z_list, label="$S_x({},{},{})$".format(self.beam_df["LoadX"][0],self.beam_df["LoadY"][0],z_list[int(self.beam_df["LoadZ"][0])]))







class Beam:
    def __init__(self, beam_geomerty_name):
        # the beam geomtry is the location of the folder that tkinter created
        self.beam_name = beam_geomerty_name
        self.input_csv = self.beam_name + r"\input.csv"
        self.input_df  = pd.read_csv(self.input_csv, header = 0, index_col = 0)
        self.ShapeName = str(self.input_df['ShapeName'][0])
        self.ShapeId   = str(self.input_df["ShapeId"][0])
        self.length =   float(str(self.input_df["Dimensions"][0]).strip('][').split(', ')[-1])



    def _run_script(self):
        # make it false if not called by analysis method
        def run(cmd):
            completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
            return completed

        #location of the script - different script for shape
        script = r"C:\Users\touze\project\Shear_centre\tkinter_trial\0.4_0.02_5.0\shape_{}.py".format(self.ShapeId)
        script_command = "abaqus cae noGUI={}".format(script)
        script_info = run(script_command)
        errormessage = str(script_info.stderr)
        print("run")
        # #need to change this to something that is connection specific
        if "Connection refused" in errormessage:
            while "Connection refused" in  errormessage:
                print("Attempting to reconnect")
                # send an email
                port = 465  # For SSL
                smtp_server = "smtp.gmail.com"
                sender_email = "shearcentre22@gmail.com"  # Enter your address
                receiver_email = "shearcentre22@gmail.com"  # Enter receiver address
                password = "Shear9922"
                message = "error"
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)

                # attempt to reconnect
                cmd = """putty.exe -load 'Abaqus license' -l 'wct24' -pw 'Wvcjmbp2299!'"""
                subprocess.run(["powershell", "-Command", cmd], capture_output=False, creationflags=subprocess.CREATE_NEW_CONSOLE)
                time.sleep(10)
                script_info = run(script_command)
                errormessage = str(script_info.stdout)
        else:
            print(errormessage)

    def _make_string_windows_compatible(self, string1):
        string1 = string1.replace(", ", "_")
        string1 = string1.replace("[", "")
        string1 = string1.replace("]", "")
        return string1

    def _navigate(self, analysis_arguments, chdir = False ):
        root = self.beam_name
        analysis_directory = root
        assert(type(analysis_arguments) == list)

        for arg in analysis_arguments:
            arg = self._make_string_windows_compatible(str(arg))
            analysis_directory = analysis_directory + r'\{}'.format(str(arg))

        # if the file doesn't exist create it
        if not os.path.exists(analysis_directory):
            os.makedirs(analysis_directory)

        if chdir==True:
            os.chdir(analysis_directory)
        return analysis_directory
    def Rotationz_at_z(self, ResultSection, abaqus_output_file_location):
        ''''takes a z position and an abaqus output file directory
                       and returns the axial rotation'''
        u = pd.read_csv(abaqus_output_file_location, header = 0, usecols = [3, 12,13,14,16,17,18])
        u.columns=["Part Instance", "x", "y", "z","U1", "U2", "U3" ]

        NoValue = "ASSEMBLY"  ## remove the loading point
        indexNames = u[u["Part Instance"]==NoValue].index

        u.drop(indexNames , inplace=True)

        u.drop(labels = "Part Instance", axis=1, inplace = True)

        u = u.astype(np.float64)

        AF = 1
        z_list = np.flip(np.unique(u["z"].values))
        z = z_list[ResultSection]
        df2 = u.loc[u["z"]==z]

        x_0 = df2["x"].values
        y_0 = df2["y"].values
        z_0 = df2["z"].values

        x_1 = x_0 + df2["U1"].values*AF
        y_1 = y_0 + df2["U2"].values*AF
        z_1 = z_0 + df2["U3"].values*AF
        A = np.vstack([x_1,y_1,z_1])
        B = np.vstack([x_0,y_0,z_0])
        assert A.shape == B.shape
        num_rows, num_cols = A.shape
        if num_rows != 3:
            raise Exception(f"matrix A is not 3xN, it is {num_rows}x{num_cols}")
        num_rows, num_cols = B.shape
        if num_rows != 3:
            raise Exception(f"matrix B is not 3xN, it is {num_rows}x{num_cols}")

        # find mean column wise
        centroid_A = np.mean(A, axis=1)
        centroid_B = np.mean(B, axis=1)

        # ensure centroids are 3x1
        centroid_A = centroid_A.reshape(-1, 1)
        centroid_B = centroid_B.reshape(-1, 1)

        # subtract mean
        Am = A - centroid_A
        Bm = B - centroid_B

        H = Am @ np.transpose(Bm)

        # find rotation
        U, S, Vt = np.linalg.svd(H)
        R = Vt.T @ U.T
        ang = mat2euler(R, axes='sxyz')

        return ang[2]


    def SimpleShearLoad(self, LoadZ, LoadX, LoadY=0.0, LoadMagnitude = -10, AnalysisType = "1. Simple_Shear_Load"):
        # print(AnalysisType)
        # print(LoadX)
        assert LoadZ < self.length*20, "LoadZ is outside the length of beam"
        assert type(LoadZ) == int, "LoadZ is a position, beam is split into 0.05m segments"

        folder_name = self._navigate([AnalysisType,"Beam_Repository", LoadZ, LoadX], chdir = True)
        print(os.path.exists(folder_name + r"\displacement.csv"))
        if not os.path.exists(folder_name + r"\displacement.csv"):
            print(LoadX)
            # if the analyis hasn't been run before - run it
            beam_data_frame = pd.DataFrame.copy(self.input_df)
            pd.options.mode.chained_assignment = None  # get rid of panda warnings
            beam_data_frame["LoadType"][0] = 1 # 1 for shear
            beam_data_frame["AnalysisType"][0] = int(AnalysisType[0])
            beam_data_frame["LoadZ"][0] = LoadZ  # always an integer
            beam_data_frame["LoadX"][0] = LoadX   # this can be anywhere
            beam_data_frame["LoadY"][0] = LoadY   # this can be anywhere but set to zero by default
            beam_data_frame["LoadMagnitude"][0] = LoadMagnitude
            beam_data_frame["LoadSection"][0] = LoadZ #No Mx allied to the section
            beam_data_frame["ResultSection"][0] = 0 #Not relevant to this type of analysis
            # print(beam_data_frame)
            beam_data_frame.to_csv('beam.csv')
            self._run_script()
        else:
            pass
        print("hello")
        return Result_Data(folder_name +r'\beam.csv',folder_name + r"\displacement.csv", folder_name + r"\stress.csv")


    def TSC(self, LoadZ, tol = 1e-5):
        """ Newton-Raphson method to find the TSC
            a small load is used to make linear"""
        AnalysisType = "2. Find_TSC"

        #load x means the x coordinate of the load
        LoadX= 0.0 #start point

        LoadX_UB = LoadX+tol
        LoadX_LB = LoadX-tol
        Rotationz_UB = -1
        Rotationz_LB = -1

        while Rotationz_UB*Rotationz_LB > 0:
            self.SimpleShearLoad(LoadZ, LoadX_UB, LoadMagnitude = -1, AnalysisType = AnalysisType)
            self.SimpleShearLoad(LoadZ, LoadX_LB, LoadMagnitude = -1, AnalysisType = AnalysisType)
            LoadX_UB_directory = self._navigate([AnalysisType,"Beam_Repository", LoadZ, LoadX_UB])
            LoadX_LB_directory = self._navigate([AnalysisType,"Beam_Repository", LoadZ, LoadX_LB])

            Rotationz_UB = self.Rotationz_at_z(0, LoadX_UB_directory +r"\displacement.csv")
            Rotationz_LB = self.Rotationz_at_z(0,LoadX_LB_directory+ r"\displacement.csv")

            # print(Rotationz_UB, Rotationz_LB )
            #newton -raphson method
            significant_digits = 10
            Rotationz_UB =  round(Rotationz_UB, significant_digits - int(math.floor(math.log10(abs(Rotationz_UB)))) - 1)
            Rotationz_LB =  round(Rotationz_LB, significant_digits - int(math.floor(math.log10(abs(Rotationz_LB)))) - 1)


            derivative_at_LoadX = (Rotationz_UB-Rotationz_LB)*50000
            Rotation_at_LoadX = (Rotationz_UB+Rotationz_LB)*0.5

            LoadX = LoadX - Rotation_at_LoadX/derivative_at_LoadX
            LoadX_UB = LoadX+tol
            LoadX_LB = LoadX-tol


        return LoadX

    def LSC(self, LoadZ, tol = 1e-5):
        """ Newton-Raphson method to find the TSC
            a small load is used to make linear"""
        AnalysisType = "3. Find_LSC"

        #load x means the x coordinate of the load
        LoadX= 0.0 #start point

        LoadX_UB = LoadX+tol
        LoadX_LB = LoadX-tol
        Rotationz_UB = -1
        Rotationz_LB = -1

        while Rotationz_UB*Rotationz_LB > 0:
            self.SimpleShearLoad(LoadZ, LoadX_UB, LoadMagnitude = -1, AnalysisType = AnalysisType)
            self.SimpleShearLoad(LoadZ, LoadX_LB, LoadMagnitude = -1, AnalysisType = AnalysisType)
            LoadX_UB_directory = self._navigate([AnalysisType,"Beam_Repository", LoadZ, LoadX_UB])
            LoadX_LB_directory = self._navigate([AnalysisType,"Beam_Repository", LoadZ, LoadX_LB])

            Rotationz_UB = self.Rotationz_at_z(int(LoadZ),LoadX_UB_directory +r"\displacement.csv")
            Rotationz_LB = self.Rotationz_at_z(int(LoadZ),LoadX_LB_directory+ r"\displacement.csv")

            # print(Rotationz_UB, Rotationz_LB )
            #newton -raphson method
            significant_digits = 10
            Rotationz_UB =  round(Rotationz_UB, significant_digits - int(math.floor(math.log10(abs(Rotationz_UB)))) - 1)
            Rotationz_LB =  round(Rotationz_LB, significant_digits - int(math.floor(math.log10(abs(Rotationz_LB)))) - 1)


            derivative_at_LoadX = (Rotationz_UB-Rotationz_LB)*50000
            Rotation_at_LoadX = (Rotationz_UB+Rotationz_LB)*0.5

            LoadX = LoadX - Rotation_at_LoadX/derivative_at_LoadX
            LoadX_UB = LoadX+tol
            LoadX_LB = LoadX-tol
        return LoadX


    def TSC_every_n_m(self,n):
        """" calculates the TSC at regular intervals down the beam and sends results to a
        datafram in the results directory"""
        assert (n/0.05)%1 == 0.0 , "n must be a multiple of 0.05 as this is the smallest devision"
        LoadZ = 0
        while LoadZ < self.length*20:
            self.TSC(LoadZ)
            LoadZ += int(20*n)


    def LSC_every_n_m(self,n):
        """" calculates the TSC at regular intervals down the beam and sends results to a
        datafram in the results directory"""
        assert (n/0.05)%1 == 0.0 , "n must be a multiple of 0.05 as this is the smallest devision"
        list_of_LoadZ =  []
        LoadZ = 0
        while LoadZ < self.length*20:
            self.LSC(LoadZ)
            LoadZ += int(20*n)





#### what's important is the location of the input csv
# beam_name = r"D:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\210.0_81.0_0.3\warping"
# input_csv = Beam_name + "input.csv"

Encatre = Beam(r"D:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\210.0_81.0_0.3\encastre")
Warping = Beam(r"D:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\210.0_81.0_0.3\Warping")

fig, ax = plt.subplots()
print(Encatre.SimpleShearLoad(0,1.0).plot_z_rotation_along_beam())
print(Warping.SimpleShearLoad(0,1.0).plot_z_rotation_along_beam())
plt.ylim(bottom=0)
plt.xlim(left=0)
ax.legend()
ax.xaxis.tick_bottom()
plt.xlabel(r'$z / m$ ', )
plt.ylabel(r'$\theta_{z}$ / \textdegree ')
plt.tight_layout()
plt.grid()
plt.show()



# sc.TSC_every_n_m(0.5)
# print("hello")
# sc.LSC_every_n_m(0.5)
#print(sc.SimpleShearLoad(89,1.0).plot_z_rotation_along_beam())






# sc.TSC(0)



















# df = pd.read_csv("input.csv", header = 0, index_col = 0)
# print(df)








# def ShearSweep(beam_number, Load_X_magnitude, LoadX_start, LoadX_end, step)
#         if df["AnalysisType"][beam_number] == 1:
#             for i in np.arange (9, 11, 1):
#                 ShearLoad(beam_number, i)
#         else:
#             print("CANNOT DO A SHEAR SWEEP ON AN ANAYSIS 3 beam")

# def get_LSC()












# if __name__ == '__main__':




