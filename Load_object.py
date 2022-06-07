import subprocess
import smtplib, ssl
import pandas as pd
import os
import time
import numpy as np
from transforms3d.euler import mat2euler, euler2mat
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patch
from matplotlib import cm
from decimal import Decimal
from shapely.geometry import Polygon
import sys
import scipy.optimize
plt.rcParams['figure.dpi'] = 1600
# sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
# from Result_Data_object import *
# from Beam_object import *
# from Section_object import *


class Load:
    def __init__(self, beam_geomerty_name):
        # the beam geomtry is the location of the folder that tkinter created
        self.beam_name = beam_geomerty_name
        self.input_csv = self._make_input_csv()
        self.input_df  = pd.read_csv(self.input_csv, header = 0, index_col = 0)
        self.ShapeName = str(self.input_df['ShapeName'][0])
        self.ShapeId   = str(self.input_df["ShapeId"][0])
        self.length =   float(str(self.input_df["Dimensions"][0]).strip('][').split(', ')[-1])

    def _make_beam_directory(self):
        beam_directory =  self.beam_name

        # if the file doesn't exist create it
        if not os.path.exists(beam_directory):
            os.makedirs(beam_directory)
        return beam_directory

    def _make_input_csv(self):
        folder_name =  self.beam_name
        # if the file doesn't exist create it
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        if not os.path.exists(folder_name + r"\input.csv"):
            #make a data frame:

            column_names =  ['ShapeName', 'ShapeId','Dimensions', "Material" , 'BoundaryCondition', 'LoadType', "AnalysisType", "LoadZ",  "LoadX",  "LoadY", "LoadMagnitude", "LoadSection", "ResultSection"]
            beam_data_frame = pd.DataFrame(columns=column_names, index=[0])

            pd.options.mode.chained_assignment = None  # get rid of panda warnings
            input_string = self.beam_name
            #there are 6 part to any beam name
            x = input_string.split( r"\\"  )
            assert len(x)==6, r"The name of the beam need to be a raw string and directory address is spaced with \\ "
            beam_data_frame["ShapeName"][0] = str(x[2])
            beam_data_frame["ShapeId"][0] = int(str(x[2])[0])
            beam_data_frame["Dimensions"][0] = list(np.float_(x[3].split( r"_" )))
            beam_data_frame["Material"][0] = list(np.float_(x[4].split( r"_" )))
            if x[5] == "warping":
                beam_data_frame["BoundaryCondition"][0] = 1
            elif x[5] == "encastre":
                beam_data_frame["BoundaryCondition"][0] = 2
            else:
                print("name error -- BCs can only be warping or encastre - no capital")
            #assign the rest of the dataframe to 0
            beam_data_frame["LoadType"][0] = 0
            beam_data_frame["AnalysisType"][0] = 0
            beam_data_frame["LoadZ"][0] = 0
            beam_data_frame["LoadX"][0] = 0.0
            beam_data_frame["LoadY"][0] = 0.0
            beam_data_frame["LoadMagnitude"][0] = 2.5
            beam_data_frame["LoadSection"][0] = 0
            beam_data_frame["ResultSection"][0] = 0
            beam_data_frame.to_csv(folder_name + r"\input.csv")
        else:
            pass
        return self.beam_name + r"\input.csv"

    def _run_script(self):
        # make it false if not called by analysis method
        def run(cmd):
            completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
            return completed

        #location of the script - different script for shape

        print(self.ShapeId)
        script = r"C:\Users\touze\project\wct24_shear_centre\abaqus_scripts\shape_{}.py".format(self.ShapeId)
        # script = r"C:\Users\touze\project\wct24_shear_centre\abaqus_scripts\shape_7.py"
        script_command = "abaqus cae script={}".format(script)
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
                cmd = """putty.exe -load 'Abaqus license' -l 'wct24' -pw '############'"""
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

    def SimpleShearLoad(self, LoadZ, LoadX, LoadY=0.0, LoadMagnitude = -1):
        # print(AnalysisType)
        # print(LoadX)
        assert LoadZ < self.length*20, "LoadZ is outside the length of beam"
        assert type(LoadZ) == int, "LoadZ is a position, beam is split into 0.05m segments"

        AnalysisType = "1. Simple_Shear_Load"
        folder_name = self._navigate([AnalysisType, "Beam_Repository", LoadMagnitude, LoadZ, LoadX], chdir = True)
        print(os.path.exists(folder_name + r"\displacement.csv"))
        print(folder_name)
        if not os.path.exists(folder_name + r"\displacement.csv"):
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
            beam_data_frame.to_csv('beam.csv')
            self._run_script()
            print("Hello")
        else:
            pass
        return Result_Data(folder_name) #+r'\beam.csv',folder_name + r"\displacement.csv", folder_name + r"\stress.csv")

    def SimpleTorqueLoad(self, LoadZ,  LoadMagnitude = -10):
        # print(AnalysisType)
        # print(LoadX)
        assert LoadZ < self.length*20, "LoadZ is outside the length of beam"
        assert type(LoadZ) == int, "LoadZ is a position, beam is split into 0.05m segments"

        AnalysisType = "4. Simple_Torque_Load"

        LoadX=0.0
        LoadY=0.0

        folder_name = self._navigate([AnalysisType,"Beam_Repository", LoadZ, LoadMagnitude], chdir = True)

        if not os.path.exists(folder_name + r"\displacement.csv"):
            # if the analyis hasn't been run before - run it
            beam_data_frame = pd.DataFrame.copy(self.input_df)
            pd.options.mode.chained_assignment = None  # get rid of panda warnings
            beam_data_frame["LoadType"][0] = 2 # 1 for Torque
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
        return Result_Data(folder_name)

    def TSC(self, LoadZ, tol = 0.5e-3):
        """ Newton-Raphson method to find the TSC
            a small load is used to make linear"""

        #load x means the x coordinate of the load
        LoadX= 0.0 #start point

        LoadX_UB = LoadX+tol
        LoadX_LB = LoadX-tol
        Rotationz_UB = -1
        Rotationz_LB = -1
        LoadMagnitude = -1

        while Rotationz_UB*Rotationz_LB > 0:
            self.SimpleShearLoad(LoadZ, LoadX_UB, LoadMagnitude = LoadMagnitude)
            self.SimpleShearLoad(LoadZ, LoadX_LB, LoadMagnitude = LoadMagnitude)
            LoadX_UB_directory = self._navigate(["1. Simple_Shear_Load","Beam_Repository", LoadMagnitude, LoadZ, LoadX_UB])
            LoadX_LB_directory = self._navigate(["1. Simple_Shear_Load","Beam_Repository", LoadMagnitude, LoadZ, LoadX_LB])

            Rotationz_UB = self.Rotationz_at_z(0, LoadX_UB_directory +r"\displacement.csv")
            Rotationz_LB = self.Rotationz_at_z(0,LoadX_LB_directory+ r"\displacement.csv")

            # print(Rotationz_UB, Rotationz_LB )
            #newton -raphson method
            significant_digits = 10
            Rotationz_UB =  round(Rotationz_UB, significant_digits - int(math.floor(math.log10(abs(Rotationz_UB)))) - 1)
            Rotationz_LB =  round(Rotationz_LB, significant_digits - int(math.floor(math.log10(abs(Rotationz_LB)))) - 1)

            print(Rotationz_UB, Rotationz_LB )
            derivative_at_LoadX = (Rotationz_UB-Rotationz_LB)/(2*tol)
            Rotation_at_LoadX = (Rotationz_UB+Rotationz_LB)*0.5

            LoadX = LoadX - Rotation_at_LoadX/derivative_at_LoadX
            LoadX_UB = LoadX+tol
            LoadX_LB = LoadX-tol

        return self.SimpleShearLoad(LoadZ, LoadX, LoadMagnitude = LoadMagnitude)

    def LSC(self, LoadZ, tol = 1e-3):
        """ Newton-Raphson method to find the LSC
            a small load is used to make linear"""
        # AnalysisType = "3. Find_LSC"

        #load x means the x coordinate of the load
        LoadX= -0.18 #start point

        LoadX_UB = LoadX+tol
        LoadX_LB = LoadX-tol
        Rotationz_UB = -1
        Rotationz_LB = -1
        LoadMagnitude = -1000
        while Rotationz_UB*Rotationz_LB > 0:
            self.SimpleShearLoad(LoadZ, LoadX_UB, LoadMagnitude = LoadMagnitude)
            self.SimpleShearLoad(LoadZ, LoadX_LB, LoadMagnitude = LoadMagnitude)
            LoadX_UB_directory = self._navigate(["1. Simple_Shear_Load","Beam_Repository", LoadMagnitude, LoadZ, LoadX_UB])
            LoadX_LB_directory = self._navigate(["1. Simple_Shear_Load","Beam_Repository", LoadMagnitude, LoadZ, LoadX_LB])

            Rotationz_UB = self.Rotationz_at_z(int(LoadZ),LoadX_UB_directory + r"\displacement.csv")
            Rotationz_LB = self.Rotationz_at_z(int(LoadZ),LoadX_LB_directory + r"\displacement.csv")

            print(Rotationz_UB, Rotationz_LB )
            #newton -raphson method
            significant_digits = 10
            Rotationz_UB =  round(Rotationz_UB, significant_digits - int(math.floor(math.log10(abs(Rotationz_UB)))) - 1)
            Rotationz_LB =  round(Rotationz_LB, significant_digits - int(math.floor(math.log10(abs(Rotationz_LB)))) - 1)


            derivative_at_LoadX = (Rotationz_UB-Rotationz_LB)/(2*tol)
            Rotation_at_LoadX = (Rotationz_UB+Rotationz_LB)*0.5

            LoadX = LoadX - Rotation_at_LoadX/derivative_at_LoadX
            LoadX_UB = LoadX+tol
            LoadX_LB = LoadX-tol
        # record the LSC

        return self.SimpleShearLoad(LoadZ, LoadX, LoadMagnitude = LoadMagnitude),LoadX

    def TSC_every_n_m(self,n):
        """" calculates the TSC at regular intervals down the beam and sends results to a
        datafram in the results directory"""
        assert (n/0.05)%1 == 0.0 , "n must be a multiple of 0.05 as this is the smallest devision"
        LoadZ = 0
        while LoadZ < self.length*20:
            self.TSC(LoadZ).GetAllWholeBeam()
            LoadZ += int(20*n)

    def LSC_every_n_m(self,n):
        """" calculates the TSC at regular intervals down the beam and sends results to a
        datafram in the results directory"""
        folder_name = self._navigate(["1. Simple_Shear_Load","Beam_Repository", -1000, "LSC"], chdir = True)
        LSC_csv =r"\LSC_every_{}m.csv".format(str(n))


        if not os.path.exists(folder_name + LSC_csv):

            assert (n/0.05)%1 == 0.0 , "n must be a multiple of 0.05 as this is the smallest devision"
            list_of_LoadZ =  []
            LoadZ = 0
            list_of_LoadX = []
            while LoadZ < self.length*20:
                LoadX = self.LSC(LoadZ)[1]

                Z = self.length -  LoadZ*0.05
                list_of_LoadX.append(LoadX)
                list_of_LoadZ.append(Z)

                LoadZ += int(20*n)

            #create the csv
            d = {"LoadX":list_of_LoadX, "LoadZ":list_of_LoadZ}
            column_names =  ["LSC"]
            LSC_df = pd.DataFrame(d)

            LSC_df.to_csv(folder_name + LSC_csv)
        else:
            LSC_df = pd.read_csv(folder_name + LSC_csv, header = 0, index_col = 0)
        LSC_df = LSC_df.astype(np.float64)
        return LSC_df

    def end_rotation_x_sweep(self,LoadZ, LoadMagnitude):
        # result_folder = self._navigate(["1. Simple_Shear_Load", "Processed_Results","sweep"])

        # sweep_csv = result_folder+ r"\end_rotation_x_sweep_{}_{}_{}_{}.csv".format(start,stop,LoadZ,LoadMagnitude)
        # if not os.path.exists(sweep_csv):
        #     #create the csv
        #     column_names =  ["Rotation", "Warping Magnitude"]
        #     sweep_df = pd.DataFrame(columns=column_names)
        #     sweep_df.index.name = "x"
        # else:
        #     sweep_df = pd.read_csv(sweep_csv, header = 0, index_col = 0)
        # sweep_df = sweep_df.astype(np.float64)

        folder = self._navigate(["1. Simple_Shear_Load", "Beam_Repository",LoadMagnitude, LoadZ])
        # print(folder)
        # os.chdir(folder)
        # print(os.listdir(folder))

        x_list = sorted([float(name) for name in os.listdir(folder)])

        for i in range(len(x_list)):
            print(x_list[i])
            self.SimpleShearLoad(LoadZ, x_list[i], LoadY=0.0, LoadMagnitude = LoadMagnitude).GetAll(0)










            #     rotation = result.section_rotationz(LoadZ)
            #     warping  = result.section_warping_magnitude(LoadZ)
            #     dfr = pd.DataFrame(data = {"Rotation":[rotation*180/np.pi],"Warping Magnitude":[warping]}, index = [x_list[i]])
            #     dfr.index.name = "x"
            #     sweep_df = sweep_df.append(dfr, ignore_index = False)
            #     print(sweep_df)
            #     sweep_df.to_csv(sweep_csv)
            # else:
            #     pass
        # return sweep_df.index, sweep_df["Rotation"].values, sweep_df["Warping Magnitude"].values



class Result_Data:
    def __init__(self, analysis_folder):
        self.analysis_folder = analysis_folder
        self.beam_csv = analysis_folder + r"\beam.csv"

        self.beam_df = pd.read_csv(self.beam_csv, header = 0,index_col=0)
        self.ShapeName = str(self.beam_df['ShapeName'][0])
        self.output_csv_displacement = analysis_folder + r"\displacement.csv"
        self.output_csv_stress = analysis_folder + r"\stress.csv"
        self.U_df = self._displacement_csv_to_data_frame(self.output_csv_displacement)
        self.S_df = self._stress_csv_to_data_frame(self.output_csv_stress)
        self.list_of_z_values = np.flip(np.unique(self.U_df["z"].values))
        self.result_folder = self._result_folder()

    def _displacement_csv_to_data_frame(self, csv_filename):
        u = pd.read_csv(csv_filename, header = 0, usecols = [3, 12,13,14,16,17,18])
        u.columns=["Part Instance", "x", "y", "z","U1", "U2", "U3" ]
        NoValue = "ASSEMBLY"  ## remove the loading point
        indexNames = u[u["Part Instance"]==NoValue].index
        u.drop(indexNames , inplace=True)
        u.drop(labels = "Part Instance", axis=1, inplace = True)
        u = u.astype(np.float64)
        return u

    def _stress_csv_to_data_frame(self, csv_filename):
        # be careful to make sure that the csv matches to the index
        s = pd.read_csv(csv_filename, header = 0, usecols = [4,5,6,7,8,22])
        s.columns=["Element", "Node","x", "y" ,"z","S33"]
        s = s.astype(np.float64)
        return s

    def _result_folder(self):
        path = self.analysis_folder + r"\results"
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def _order_points(pts):
        # sort the points based on their x-coordinates
        xSorted = pts[np.argsort(pts[:, 0]), :]
        # grab the left-most and right-most points from the sorted
        # x-roodinate points
        leftMost = xSorted[:2, :]
        rightMost = xSorted[2:, :]
        # now, sort the left-most coordinates according to their
        # y-coordinates so we can grab the top-left and bottom-left
        # points, respectively
        leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
        (tl, bl) = leftMost
        # now that we have the top-left coordinate, use it as an
        # anchor to calculate the Euclidean distance between the
        # top-left and right-most points; by the Pythagorean
        # theorem, the point with the largest distance will be
        # our bottom-right point
        D = dist.cdist(tl[np.newaxis], rightMost, "euclidean")[0]
        (br, tr) = rightMost[np.argsort(D)[::-1], :]
        # return the coordinates in top-left, top-right,
        # bottom-right, and bottom-left order
        return np.array([tl, tr, br, bl], dtype="float64")

    def _element_list(self, z):
        """ returns a list of connected nodes
            1. find the element the node belongs to
            2. find the coordinates of all the nodes in the element"""
        DF = self.S_df.loc[self.S_df["z"]==z]

        DF.drop(labels = "z", axis=1, inplace = True)
        element_labels = np.flip(np.unique(DF["Element"].values))
        # condition = (DF['x'] ==x) & (DF['y'] == y)
        # b = DF.index[condition].tolist()
        # element = DF.loc[b]["Element"].values[0]
        # print(element)

        element_array = an_array = np.full([len(element_labels)], None)
        n = 0
        for element in element_labels:
            condition = (DF['Element'] ==element)
            b = DF.index[condition].tolist()
            xy = DF.loc[b]
            x = xy["x"].values.T
            y = xy["y"].values.T
            XY = np.array(list(zip(x,y)))

            x_centroid = np.mean(x)
            y_centroid = np.mean(y)

            # for xy in XY:
            #     if xy[0] <= x_centroid and xy[1] >= y_centroid:
            #         tl = xy

            #     elif xy[0] > x_centroid and xy[1] >= y_centroid:
            #         tr = xy
            #     elif xy[0] > x_centroid and xy[1] <= y_centroid:
            #         br = xy
            #     elif xy[0] < x_centroid and xy[1] <= y_centroid:
            #         bl = xy
            #     else:
            #         print("error")
            xSorted = XY[XY[:, 0].argsort()]
            y_sorted = XY[XY[:, 1].argsort()]
            leftMost = xSorted[:2, :]
            rightMost = xSorted[2:, :]

            leftMost = leftMost[leftMost[:, 1].argsort()]
            (tl, bl) = leftMost



            rightMost = rightMost[rightMost[:, 1].argsort()]
            (tr, br) = rightMost
            # element = self._order_points(element)
            element_array[n] = (tl[0], tl[1], tr[0],tr[1],br[0],br[1], bl[0], bl[1])
            n+=1
        return element_array

    def section_rotationz(self, ResultSection):
        ''''takes a z coordinate and an abaqus output file directory and returns the axial rotation'''
        section_rotationz_csv = self.result_folder+ r"\section_rotationz.csv"
        if not os.path.exists(section_rotationz_csv ):
            #create the csv
            column_names =  ["Rotation"]
            Rz_df = pd.DataFrame(columns=column_names)
            Rz_df.index.name = "z"
        else:
            Rz_df = pd.read_csv(section_rotationz_csv, header = 0, index_col = 0)
        Rz_df = Rz_df.astype(np.float64)



        z = self.list_of_z_values[ResultSection]
        if z not in Rz_df.index:
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

            dfr = pd.DataFrame(data = {"Rotation":[ang[2]]}, index = [z])
            dfr.index.name = "z"
            Rz_df = Rz_df.append(dfr, ignore_index = False)
            Rz_df.to_csv(section_rotationz_csv)


        z_rotation = Rz_df.loc[z,"Rotation"]
        return z_rotation

    def z_rotation_along_beam(self):

        rotationz_list =[]
        for i in range(len(self.list_of_z_values)):
            rotationz_list.append(self.section_rotationz(i)*180/np.pi)
        z_list = self.list_of_z_values
        # ax.plot(z_list, rotation_z_list, label="$S_x({},{},{})$".format(self.beam_df["LoadX"][0],self.beam_df["LoadY"][0],z_list[int(self.beam_df["LoadZ"][0])]))
        return z_list, rotationz_list

    def _get_twist(self, ResultSection):
        if ResultSection == 0:
            d_theta = self.section_rotationz(ResultSection) - self.section_rotationz(ResultSection+1)
            dz = self.list_of_z_values[ResultSection]-self.list_of_z_values[ResultSection+1]
            dtheta_dz = d_theta/dz
        elif ResultSection == len(self.list_of_z_values)-1:
            d_theta = self.section_rotationz(ResultSection-1) - self.section_rotationz(ResultSection)
            dz = self.list_of_z_values[ResultSection-1]-self.list_of_z_values[ResultSection]
            dtheta_dz = d_theta/dz
        else:
            d_theta = self.section_rotationz(ResultSection-1) - self.section_rotationz(ResultSection+1)
            dz = self.list_of_z_values[ResultSection-1]-self.list_of_z_values[ResultSection+1]
            dtheta_dz = d_theta/dz
        # remove floating point error
        significant_digits = 10
        Twist =  round(dtheta_dz, significant_digits - int(math.floor(math.log10(abs(dtheta_dz)))) - 1)
        return Twist

    def _get_twist_derivative(self, ResultSection):
        if ResultSection == 0:
            d_theta = self._get_twist(ResultSection) - self._get_twist(ResultSection+1)
            dz = self.list_of_z_values[ResultSection]-self.list_of_z_values[ResultSection+1]
            dtheta_dz = d_theta/dz
        elif ResultSection == len(self.list_of_z_values)-1:
            d_theta = self._get_twist(ResultSection-1) - self._get_twist(ResultSection)
            dz = self.list_of_z_values[ResultSection-1]-self.list_of_z_values[ResultSection]
            dtheta_dz = d_theta/dz
        else:
            d_theta = self._get_twist(ResultSection-1) - self._get_twist(ResultSection+1)
            dz = self.list_of_z_values[ResultSection-1]-self.list_of_z_values[ResultSection+1]
            dtheta_dz = d_theta/dz
        # remove floating point error
        significant_digits = 10

        Twist =  round(dtheta_dz, significant_digits - int(math.floor(math.log10(abs(dtheta_dz)))) - 1)
        return Twist

    def GetAllSingleSection(self, ResultSection):
           # get the z coordinates of the sections
        # get the z coordinates of the sections
        z = self.list_of_z_values[ResultSection]
        main_information_csv  = self.result_folder+ "\\main_information.csv"
        extra_information_csv = self.result_folder+ "\\extra_information"+ "\\{}.csv".format(str(z))

        if not os.path.exists(main_information_csv):
            #create the csv
            column_names =  []
            main_df = pd.DataFrame(columns=column_names)
            main_df.index.name = "z"
        else:
            main_df = pd.read_csv(main_information_csv, header = 0, index_col = 0)
        main_df = main_df.astype(np.float64)

        if not os.path.exists(self.result_folder+ "\\extra_information"):
            os.mkdir(self.result_folder+ "\\extra_information")
        else:
            pass

        if not os.path.exists(extra_information_csv):
            #create the csv
            column_names =  []
            extra_df = pd.DataFrame(columns=column_names)
            extra_df.index.name = "e"
        else:
            extra_df = pd.read_csv(extra_information_csv, header = 0, index_col = 0)
        extra_df = extra_df.astype(np.float64)

        # only runs if it hasn't run before
        # print(main_df.index)
        # print(z)
        if z not in main_df.index:
            df1 = self.U_df.loc[self.U_df["z"]==z]
            element_array = self._element_list(z)
            # the element will appear twice once downbeam and once up beam for a 3D element
            element_array = np.unique(element_array)
            df1 = df1.reset_index()

            x_0 = df1["x"].values
            y_0 = df1["y"].values
            z_0 = np.zeros(np.shape(y_0))
            # plt.scatter(x_0[1:100], y_0[1:100], z_0[1:100])
            # warping_displacement =

            # find the rotation:
            x_1 = x_0 + df1["U1"].values
            y_1 = y_0 + df1["U2"].values
            z_1 = df1["U3"].values

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

            GlobalDisplacementVector = centroid_B - centroid_A

            # subtract mean
            Am = A - centroid_A
            Bm = B - centroid_B

            H = Am @ np.transpose(Bm)
            U, S, Vt = np.linalg.svd(H)
            R = Vt.T @ U.T

            GlobalRotationVector = mat2euler(R, axes='sxyz')

            # if abs(GlobalRotationVector[0])>2:
            #     GlobalRotationVectorX = GlobalRotationVector[0] + np.pi
            #     R = euler2mat(GlobalRotationVector[0], GlobalRotationVectorX,GlobalRotationVector[2])
            #     GlobalRotationVector = (GlobalRotationVectorX, GlobalRotationVector[1],GlobalRotationVector[2])


            # if abs(GlobalRotationVector[1])>2:
            #     GlobalRotationVectorY = GlobalRotationVector[1] + np.pi
            #     R = euler2mat(GlobalRotationVector[0], GlobalRotationVectorY,GlobalRotationVector[2])

            t = -R @ centroid_A + centroid_B
            XYZ_2  = R @ A + t

            x_2 = XYZ_2[0]
            y_2 = XYZ_2[1]
            w_2 = XYZ_2[2]


            MaxWarp = w_2.max()
            MinWarp = w_2.min()

            #inatilise the overal variables

            warping_magnitude = 0.0
            stress_magnitude =0.0
            Area = 0.0
            wc = np.zeros((np.shape(element_array)[0],2), dtype=np.float64)
            rc = np.zeros((np.shape(element_array)[0],2), dtype=np.float64)
            sc = np.zeros((np.shape(element_array)[0],2), dtype=np.float64)
            J = 0.0


            df2 = self.S_df.loc[self.S_df["z"]==z]
            MaxStress = df2["S33"].max()
            MinStress = df2["S33"].min()

            for i in range(np.shape(element_array)[0]):
                ###############################################################################################
                #warping
                ###############################################################################################
                (X0_0,Y0_0,X1_0,Y1_0, X2_0,Y2_0, X3_0,Y3_0) = element_array[i]
                AFxy = 1
                AFz  = 1
                print("---------------")
                condition = (df1['x'] == X0_0) & (df1['y'] == Y0_0)
                b = df1.index[condition].tolist()
                # print(b)
                X0_2 = x_2[b[0]]
                Y0_2 = y_2[b[0]]
                X0_1 = x_1[b[0]]
                Y0_1 = y_1[b[0]]
                W0 = w_2[b[0]]

                condition = (df1['x'] == X1_0) & (df1['y'] == Y1_0)
                b = df1.index[condition].tolist()
                # print(b)

                X1_2 = x_2[b[0]]
                Y1_2 = y_2[b[0]]
                X1_1 = x_1[b[0]]
                Y1_1 = y_1[b[0]]
                W1 = w_2[b[0]]

                condition = (df1['x'] == X2_0) & (df1['y'] == Y2_0)
                b = df1.index[condition].tolist()

                # print(b)
                X2_2 = x_2[b[0]]
                Y2_2 = y_2[b[0]]
                X2_1 = x_1[b[0]]
                Y2_1 = y_1[b[0]]
                W2 = w_2[b[0]]

                condition = (df1['x'] == X3_0) & (df1['y'] == Y3_0)
                b = df1.index[condition].tolist()

                # print(b)
                X3_2 = x_2[b[0]]
                Y3_2 = y_2[b[0]]
                X3_1 = x_1[b[0]]
                Y3_1 = y_1[b[0]]
                W3 = w_2[b[0]]

                X2 = [X0_2, X1_2, X2_2, X3_2]
                X1 = [X0_1, X1_1, X2_1, X3_1]
                X0 = [X0_0, X1_0, X2_0, X3_0]
                Y2 = [Y0_2, Y1_2, Y2_2, Y3_2]
                Y1 = [Y0_1, Y1_1, Y2_1, Y3_1]
                Y0 = [Y0_0, Y1_0, Y2_0, Y3_0]

                centroid_x = np.mean(X2)
                centroid_y = np.mean(Y2)
                assert Y0_2-Y2_2 <0.1

                W = [W0, W1, W2, W3]

                dArea = Polygon(zip(X2, Y2)).area # Assuming the OP's x,y coordinates

                Area += dArea

                #########################################################################
                #Warping
                #########################################################################
                Twist = self._get_twist(ResultSection)

                points = np.array([[0,2],[1,3]])
                dw_array = np.zeros(len(points))
                S = np.zeros(np.shape(points))
                n=0
                for point in points:
                    ds = np.array([(X0[point[1]]-X0[point[0]]),(Y0[point[1]]-Y0[point[0]]), 0])
                    dw = (W[point[1]] -W[point[0]])/Twist
                    #vector from centroid of the element to centre of the segment
                    a = (X0[point[1]]+X0[point[0]])/2 - centroid_x
                    b = (Y0[point[1]]+Y0[point[0]])/2 - centroid_y
                    # plt.plot([a+centroid_x,centroid_x],[b+centroid_y,centroid_y] )
                    r = np.array([centroid_x+a-0.4*4/np.pi, centroid_y+b, 0])
                    dw_array[n] = dw-np.cross([a,b,0], ds)[-1]
                    S[n] = [ds[1], -ds[0]]
                    n+=1


                x_wc_, y_wc_ = (np.linalg.lstsq(S, dw_array, rcond=None)[0])
                x_wc, y_wc = [centroid_x-x_wc_,centroid_y-y_wc_]
                wc[i] = [x_wc,y_wc]
                warping_magnitude += np.mean(W)**2*dArea
                # ###############################################################################################
                # #Rotation
                # ###############################################################################################

                m_array = np.zeros(4)
                c_array = np.zeros(4)

                X1 = [X0_1, X1_1, X2_1, X3_1]
                X0 = [X0_0, X1_0, X2_0, X3_0]

                Y1 = [Y0_1, Y1_1, Y2_1, Y3_1]
                Y0 = [Y0_0, Y1_0, Y2_0, Y3_0]

                for k in range(4):
                    v1 = np.array([X1[k]-X0[k], Y1[k]-Y0[k]])
                    v1_unit = v1/np.linalg.norm(v1)
                    v1_perpendicular = np.matmul(np.array([[0,-1],[1,0]]),v1)
                    m= v1_perpendicular[1]/v1_perpendicular[0]
                    c = -m*X0[k]+Y0[k]
                    m_array[k] = m
                    c_array[k] = c

                A = np.vstack([-m_array, np.ones(len(m_array))]).T
                x_rc, y_rc = (np.linalg.lstsq(A, c_array, rcond=None)[0])
                rc[i] = [x_rc, y_rc]

                # ###############################################################################################
                # #stress
                # ###############################################################################################
                TwistDerivative = self._get_twist_derivative(ResultSection)

                condition = (df2['x'] == X0_0) & (df2['y'] == Y0_0)
                b = df2.index[condition].tolist()
                S0 = df2["S33"][b[0]]

                condition = (df2['x'] == X1_0) & (df2['y'] == Y1_0)
                b = df2.index[condition].tolist()
                S1 = df2["S33"][b[0]]

                condition = (df2['x'] == X2_0) & (df2['y'] == Y2_0)
                b = df2.index[condition].tolist()
                S2 = df2["S33"][b[0]]

                condition = (df2['x'] == X3_0) & (df2['y'] == Y3_0)
                b = df2.index[condition].tolist()
                S3 = df2["S33"][b[0]]

                s_mean = (S0+S1+S2+S3)/4
                stress_magnitude += abs(s_mean)*dArea

                Stress = [S0, S1, S2, S3]

                ###############
                #Inset stress code here
                ###############

                points = np.array([[0,2],[1,3]])
                dstress_array = np.zeros(len(points))
                S = np.zeros(np.shape(points))
                n=0
                for point in points:
                    ds = np.array([(X0[point[1]]-X0[point[0]]),(Y0[point[1]]-Y0[point[0]]), 0])
                    dstress = (Stress[point[1]] -Stress[point[0]])/(TwistDerivative*210*10**6)
                    #vector from centroid of the element to centre of the segment
                    a = (X0[point[1]]+X0[point[0]])/2 - centroid_x
                    b = (Y0[point[1]]+Y0[point[0]])/2 - centroid_y
                    # plt.plot([a+centroid_x,centroid_x],[b+centroid_y,centroid_y] )
                    r = np.array([centroid_x+a-0.4*4/np.pi, centroid_y+b, 0])
                    dstress_array[n] = dstress-np.cross([a,b,0], ds)[-1]
                    S[n] = [ds[1], -ds[0]]
                    n+=1
                x_sc_, y_sc_ = (np.linalg.lstsq(S, dstress_array, rcond=None)[0])
                x_sc, y_sc = [centroid_x-x_sc_,centroid_y-y_sc_]
                sc[i] = [x_sc, y_sc]
                #################################################################
                #saint-venant constant
                ##################################################################
                J1 = 0.0
                J2 = 0.0
                J3 = 0.0
                J4 = 0.0


                X2_centroid = centroid_x
                Y2_centroid = centroid_y
                integral1 = (X2_centroid-x_rc)**2
                integral2 = (Y2_centroid-y_rc)**2
                integral3 = (X2_centroid-x_rc)*(X2_centroid-x_wc)
                integral4 = (Y2_centroid-y_rc)*(Y2_centroid-y_wc)

                J1 += integral1*dArea
                J2 += integral2*dArea
                J3 += integral3*dArea
                J4 += integral4*dArea
                j = J1-J3+J2-J4
                J += j
                data = {
                    "X0_0" : X0_0,
                    "Y0_0" : Y0_0,
                    "X1_0" : X1_0,
                    "Y1_0" : Y1_0,
                    "X2_0" : X2_0,
                    "Y2_0" : Y2_0,
                    "X3_0" : X3_0,
                    "Y3_0" : Y3_0,
                    "X0_1" : X0_1,
                    "Y0_1" : Y0_1,
                    "X1_1" : X1_1,
                    "Y1_1" : Y1_1,
                    "X2_1" : X2_1,
                    "Y2_1" : Y2_1,
                    "X3_1" : X3_1,
                    "Y3_1" : Y3_1,
                    "X0_2" : X0_2,
                    "Y0_2" : Y0_2,
                    "X1_2" : X1_2,
                    "Y1_2" : Y1_2,
                    "X2_2" : X2_2,
                    "Y2_2" : Y2_2,
                    "X3_2" : X3_2,
                    "Y3_2" : Y3_2,
                    "W0"   : W0,
                    "W1"   : W1,
                    "W2"   : W2,
                    "W3"   : W3,
                    "S0"   : S0,
                    "S1"   : S1,
                    "S2"   : S2,
                    "S3"   : S3,
                    "x_wc" : x_wc,
                    "y_wc" : y_wc,
                    "x_sc" : x_sc,
                    "y_sc" : y_sc,
                    "x_rc" : x_rc,
                    "y_rc" : y_rc,
                    }
                dfr = pd.DataFrame(data = data, index = [i] )
                dfr.index.name = "e"
                extra_df = extra_df.append(dfr, ignore_index = False)
                extra_df.to_csv(extra_information_csv)


            StressMagnitude = stress_magnitude/Area
            WarpingMagnitude = np.sqrt(warping_magnitude/Area)

            MeanWC = np.mean(wc, axis=0)
            MeanRC = np.mean(rc, axis=0)
            MeanSC = np.mean(sc, axis=0)

            SpreadWC = np.linalg.norm(np.std(wc, axis=0))
            SpreadRC = np.linalg.norm(np.std(rc, axis=0))
            SpreadSC = np.linalg.norm(np.std(sc, axis=0))

            data = {
                "GlobalDisplacementVectorX": GlobalDisplacementVector.T[0][0],
                "GlobalDisplacementVectorY": GlobalDisplacementVector.T[0][1],
                "GlobalDisplacementVectorZ": GlobalDisplacementVector.T[0][2],
                "GlobalRotationVectorX": GlobalRotationVector[0],
                "GlobalRotationVectorY": GlobalRotationVector[1],
                "GlobalRotationVectorZ": GlobalRotationVector[2],
                "Area": Area,
                "Twist": Twist,
                "TwistDerivative": TwistDerivative,
                "WarpingMagnitude": WarpingMagnitude,
                "MaxWarp": MaxWarp,
                "MinWarp": MinWarp,
                "StressMagnitude": StressMagnitude,
                "MaxStress": MaxStress,
                "MinStress": MinStress,
                "MeanRCX": MeanRC[0],
                "MeanRCY": MeanRC[1],
                "SpreadRC": SpreadRC,
                "MeanWCX": MeanWC[0],
                "MeanWCY": MeanWC[1],
                "SpreadWC": SpreadWC,
                "MeanSCX": MeanSC[0],
                "MeanSCY": MeanSC[1],
                "SpreadSC": SpreadSC,
                "J": J,
            }
            dfr = pd.DataFrame(data = data, index = [z])
            dfr.index.name = "z"
            main_df = main_df.append(dfr, ignore_index = False)
            main_df.to_csv(main_information_csv)

        return Section(main_df, extra_df, z,self.analysis_folder)

    def GetAllWholeBeam(self):
        z = self.list_of_z_values
        main_information_csv  = self.result_folder+ "\\main_information.csv"
        if not os.path.exists(main_information_csv):
            #create the csv
            for i in range(len(self.list_of_z_values)-2):
                print(i)
                self.GetAllSingleSection(i)

        main_df = pd.read_csv(main_information_csv, header = 0, index_col = 0)
        main_df = main_df.astype(np.float64)
        return Beam(main_df,z,self.analysis_folder)

    def warping_magnitude_along_beam(self, include_stress=False):
        warping_list =[]
        stress_list = []
        for i in range(len(self.list_of_z_values)):
            warping_list.append(self.section_warping_magnitude(i,include_stress=include_stress)[0])
            stress_list.append(self.section_warping_magnitude(i,include_stress=include_stress)[1])
        z_list = self.list_of_z_values
        # ax.plot(z_list, rotation_z_list, label="$S_x({},{},{})$".format(self.beam_df["LoadX"][0],self.beam_df["LoadY"][0],z_list[int(self.beam_df["LoadZ"][0])]))
        return z_list, warping_list, stress_list

    def plot_deformed_cross_section_3D_combind(self,LoadZ):
        # get the z coordinates of the sections
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        # get the z coordinates of the sections


        maximum_warp = 1000*w.max()
        minimum_warp = 1000*w.min()

        maximum_x = x_2.max()
        minimum_x = x_2.min()

        maximum_y = y_2.max()
        minimum_y = y_2.min()

        for i in range(np.shape(element_array)[0]):
            [X0_0,Y0_0,X1_0,Y1_0, X2_0,Y2_0, X3_0,Y3_0] = element_array[i]
            AFxy = 1
            AFz  = 1
            condition = (df1['x'] == X0_0) & (df1['y'] == Y0_0)
            b = df1.index[condition].tolist()
            X0_1 = x_2[b[0]]
            Y0_1 = y_2[b[0]]
            W0 = w[b[0]]*1000
            condition = (df1['x'] == X1_0) & (df1['y'] == Y1_0)
            b = df1.index[condition].tolist()
            X1_1 = x_2[b[0]]
            Y1_1 = y_2[b[0]]
            W1 = w[b[0]]*1000

            condition = (df1['x'] == X2_0) & (df1['y'] == Y2_0)
            b = df1.index[condition].tolist()
            X2_1 = x_2[b[0]]
            Y2_1 = y_2[b[0]]
            W2 = w[b[0]]*1000

            condition = (df1['x'] == X3_0) & (df1['y'] == Y3_0)
            b = df1.index[condition].tolist()
            X3_1 = x_2[b[0]]
            Y3_1 = y_2[b[0]]
            W3 = w[b[0]]*1000


            cf = ax.plot_surface(np.array([[X0_0,X1_0],[X3_0,X2_0]]),np.array([[Y0_0,Y1_0],[Y3_0,Y2_0]]), np.array([[0.0,0.0],[0.0,0.0]]), color = (0.1,0.1,0.1, 0.5))
            ax.plot_surface(np.array([[X0_1,X1_1],[X3_1,X2_1]]),np.array([[Y0_1,Y1_1],[Y3_1,Y2_1]]), np.array([[W0,W1],[W3,W2]]),vmin=minimum_warp, vmax=maximum_warp, rstride=1, cstride=1, cmap=cm.seismic,linewidth=0.3, antialiased=False, edgecolor=(0,0,0,1))

            #need to get the colour for the contour plot

            cmap = cf.get_cmap()


            seismic = cm.get_cmap('seismic', 256)
            # avaerage warping as a number from 1 to 256


            def get_colour():
                mean_warp = (W0+W1+W2+W3)/4
                range_w =  maximum_warp-minimum_warp
                Float_between_0_and_1 = (mean_warp-minimum_warp)/range_w
                return Float_between_0_and_1


            z_offset = minimum_warp - 0.2*(maximum_warp-minimum_warp)

            ax.plot_surface(np.array([[X0_1,X1_1],[X3_1,X2_1]]),np.array([[Y0_1,Y1_1],[Y3_1,Y2_1]]), np.array([[z_offset,z_offset],[z_offset,z_offset]]), color = seismic(get_colour()), shade=False)
            y_offset = maximum_y + 0.2*(maximum_y-minimum_y)
            ax.plot_surface(np.array([[X0_1,X1_1],[X3_1,X2_1]]),np.array([[y_offset,y_offset],[y_offset,y_offset]]), np.array([[W0,W1],[W3,W2]]), color = seismic(get_colour()),shade=False)
            x_offset = minimum_x - 0.2*(maximum_x-minimum_x)

            ax.plot_surface(np.array([[x_offset ,x_offset ],[x_offset , x_offset]]),np.array([[Y0_1,Y1_1],[Y3_1,Y2_1]]), np.array([[W0,W1],[W3,W2]]), color = seismic(get_colour()), shade=False)

        ax.set_zlim(bottom= z_offset*0.97, top = -z_offset*0.97)
        ax.set_xlim(left=x_offset *0.97)
        ax.set_ylim(top=y_offset*0.97)
        ax.locator_params(axis='z', nbins=5)
        # ax.set_zticklabels([maximum_warp, minimum_warp])

        ax.set_box_aspect([1,(maximum_y-minimum_y)/(maximum_x-minimum_x),1])

        ax.set_xlabel("$x / m$")
        ax.set_ylabel("$z / m$")
        ax.set_zlabel("$w / mm$")


        fig.set_figwidth(6.29921)
        fig.set_dpi(500)

        plt.tight_layout()
        folder_name = r"D:\\report\\figs"+r"\\"+self.ShapeName+ r"\graph_4"

        if not os.path.exists(folder_name ):
            os.makedirs(folder_name)

        plt.savefig(folder_name+r"\graph_4_1.png")
        plt.savefig(folder_name+r"\graph_4_1.pgf")


        # radius = np.sqrt(centroid_x**2 + centroid_y**2)
        # if radius > 0.4:
        #     if centroid_y > 0:
        #         plt.scatter([wc[0][0]],[wc[0][1]], color="blue")
        #     else:
        #         plt.scatter([wc[0][0]],[wc[0][1]], color="green")

        # else:
        #     if centroid_y > 0:
        #         plt.scatter([wc[0][0]],[wc[0][1]], color="red")
        #     else:
        #         plt.scatter([wc[0][0]],[wc[0][1]], color="orange")

    def magnitude_of_w(self):
        return 0




class Section(Result_Data):
    def __init__(self, main_df,extra_df,z, analyis_folder):
        self.analyis_folder = analyis_folder
        Result_Data.__init__(self, self.analyis_folder)
        self.main_df = main_df
        self.extra_df = extra_df
        self.z = z

    def _make_string_linux_compatible(self, string1):
        string1 = string1.replace(", ", "_")
        string1 = string1.replace(".", "_")
        string1 = string1.replace("[", "")
        string1 = string1.replace("]", "")
        return string1

    def plot_deformed_cross_section_3D(self, contours = True, write_up=False):
        # get the z coordinates of the sections
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        # get the z coordinates of the sections


        maximum_warp = 1000*self.main_df["MaxWarp"][self.z]
        minimum_warp = 1000*self.main_df["MinWarp"][self.z]



        maximum_x = self.extra_df["X0_0"].max()
        minimum_x = self.extra_df["X0_0"].min()

        maximum_y = self.extra_df["Y0_0"].max()
        minimum_y = self.extra_df["Y0_0"].min()
        for index, row in self.extra_df.iterrows():
            cf = ax.plot_surface(np.array([[row["X0_0"],row["X1_0"]],[row["X3_0"],row["X2_0"]]]),np.array([[row["Y0_0"],row["Y1_0"]],[row["Y3_0"],row["Y2_0"]]]), 1000*np.array([[0.0,0.0],[0.0,0.0]]), color = (0.1,0.1,0.1, 0.5))


            ax.plot_surface(np.array([[row["X0_2"],row["X1_2"]],[row["X3_2"],row["X2_2"]]]),np.array([[row["Y0_2"],row["Y1_2"]],[row["Y3_2"],row["Y2_2"]]]), 1000*np.array([[row["W0"],row["W1"]],[row["W3"],row["W2"]]]),vmin=minimum_warp, vmax=maximum_warp, rstride=1, cstride=1, cmap=cm.plasma,linewidth=0.1, antialiased=False, edgecolor=(0.1,0.1,0.1,0.5))

            #need to get the colour for the contour plot

            cmap = cf.get_cmap()


            seismic = cm.get_cmap('seismic', 256)
            # avaerage warping as a number from 1 to 256


            def get_colour():
                mean_warp = 1000*(row["W0"]+row["W1"]+row["W2"]+row["W2"])/4
                range_w =  maximum_warp-minimum_warp
                Float_between_0_and_1 = (mean_warp-minimum_warp)/range_w
                return Float_between_0_and_1


            z_offset = minimum_warp - 0.2*(maximum_warp-minimum_warp)

            ax.plot_surface(np.array([[row["X0_2"],row["X1_2"]],[row["X3_2"],row["X2_2"]]]),np.array([[row["Y0_2"],row["Y1_2"]],[row["Y3_2"],row["Y2_2"]]]), np.array([[z_offset,z_offset],[z_offset,z_offset]]), color = seismic(get_colour()), shade=False)
            y_offset = maximum_y + 0.2*(maximum_y-minimum_y)
            ax.plot_surface(np.array([[row["X0_2"],row["X1_2"]],[row["X3_2"],row["X2_2"]]]),np.array([[y_offset,y_offset],[y_offset,y_offset]]), 1000*np.array([[row["W0"],row["W1"]],[row["W3"],row["W2"]]]), color = seismic(get_colour()),shade=False)
            x_offset = minimum_x - 0.2*(maximum_x-minimum_x)

            ax.plot_surface(np.array([[x_offset ,x_offset ],[x_offset , x_offset]]),np.array([[row["Y0_2"],row["Y1_2"]],[row["Y3_2"],row["Y2_2"]]]), 1000*np.array([[row["W0"],row["W1"]],[row["W3"],row["W2"]]]), color = seismic(get_colour()), shade=False)


        ax.set_zlim(bottom= z_offset*0.97, top = -z_offset*0.97)
        ax.set_xlim(left=x_offset *0.97)
        ax.set_ylim(top=y_offset*0.97)

        ax.locator_params(axis='z', nbins=5)
        # ax.set_zticklabels([maximum_warp, minimum_warp])



        ax.set_box_aspect([1,(maximum_y-minimum_y)/(maximum_x-minimum_x),1])

        ax.set_xlabel("$x / m$")
        ax.set_ylabel("$z / m$")
        ax.set_zlabel("$w / mm$")


        fig.set_figwidth(6.29921)
        fig.set_dpi(1000)

        plt.tight_layout()
        folder_name = self.result_folder + "\\graphs" + "\\{}".format(str(self.z))


        if not os.path.exists(folder_name ):
            os.makedirs(folder_name)

        plt.savefig(folder_name+r"\plot_deformed_cross_section_3D_section_z_{}.png".format(str(self.z)))
        plt.savefig(folder_name+r"\plot_deformed_cross_section_3D_section_z_{}.pgf".format(str(self.z)))



        if write_up == True:
            write_up_folder = self.result_folder.replace("shear_centre", "report\\figs")
            if not os.path.exists(write_up_folder ):
                os.makedirs(write_up_folder)
            plt.savefig(write_up_folder+r"\plot_deformed_cross_section_3D_section_z_{}.png".format(str(int(self.z*100))))
            plt.savefig(write_up_folder+r"\plot_deformed_cross_section_3D_section_z_{}.pgf".format(str(int(self.z*100))))

    def plot_warping_function(self, contours = True, write_up=False):
        # get the z coordinates of the sections
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        # get the z coordinates of the sections
        fig.set_dpi(1200)

        Twist = self.main_df["Twist"][self.z]


        maximum_omega = self.main_df["MaxWarp"][self.z]/Twist
        minimum_omega = self.main_df["MinWarp"][self.z]/Twist



        maximum_x = self.extra_df["X0_0"].max()
        minimum_x = self.extra_df["X0_0"].min()

        maximum_y = self.extra_df["Y0_0"].max()
        minimum_y = self.extra_df["Y0_0"].min()
        for index, row in self.extra_df.iterrows():
            cf = ax.plot_surface(np.array([[row["X0_0"],row["X1_0"]],[row["X3_0"],row["X2_0"]]]),np.array([[row["Y0_0"],row["Y1_0"]],[row["Y3_0"],row["Y2_0"]]]), (1/Twist)*np.array([[0.0,0.0],[0.0,0.0]]), color = (0.1,0.1,0.1, 0.5))


            ax.plot_surface(np.array([[row["X0_2"],row["X1_2"]],[row["X3_2"],row["X2_2"]]]),np.array([[row["Y0_2"],row["Y1_2"]],[row["Y3_2"],row["Y2_2"]]]), (1/Twist)*np.array([[row["W0"],row["W1"]],[row["W3"],row["W2"]]]),vmin=minimum_omega, vmax=maximum_omega, rstride=1, cstride=1, cmap=cm.plasma,linewidth=0.1, antialiased=False, edgecolor=(0.1,0.1,0.1,0.5))

            #need to get the colour for the contour plot

            cmap = cf.get_cmap()


            seismic = cm.get_cmap('seismic', 256)
            # avaerage warping as a number from 1 to 256


            def get_colour():
                mean_omega = (1/Twist)*(row["W0"]+row["W1"]+row["W2"]+row["W2"])/4
                range_w =  maximum_omega-minimum_omega
                Float_between_0_and_1 = (mean_omega-minimum_omega)/range_w
                return Float_between_0_and_1


            z_offset = minimum_omega - 0.2*(maximum_omega-minimum_omega)

            ax.plot_surface(np.array([[row["X0_2"],row["X1_2"]],[row["X3_2"],row["X2_2"]]]),np.array([[row["Y0_2"],row["Y1_2"]],[row["Y3_2"],row["Y2_2"]]]), np.array([[z_offset,z_offset],[z_offset,z_offset]]), color = seismic(get_colour()), shade=False)
            y_offset = maximum_y + 0.3*(maximum_y-minimum_y)
            ax.plot_surface(np.array([[row["X0_2"],row["X1_2"]],[row["X3_2"],row["X2_2"]]]),np.array([[y_offset,y_offset],[y_offset,y_offset]]), (1/Twist)*np.array([[row["W0"],row["W1"]],[row["W3"],row["W2"]]]), color = seismic(get_colour()),shade=False)
            x_offset = minimum_x - 0.5*(maximum_x-minimum_x)

            ax.plot_surface(np.array([[x_offset ,x_offset ],[x_offset , x_offset]]),np.array([[row["Y0_2"],row["Y1_2"]],[row["Y3_2"],row["Y2_2"]]]), (1/Twist)*np.array([[row["W0"],row["W1"]],[row["W3"],row["W2"]]]), color = seismic(get_colour()), shade=False)


        ax.set_zlim(bottom= z_offset*0.97, top = -z_offset*0.97)
        ax.set_xlim(left=x_offset *0.97)
        ax.set_ylim(top=y_offset*0.97)

        ax.locator_params(axis='z', nbins=5)
        ax.locator_params(axis='x', nbins=5)

        # ax.set_zticklabels([maximum_warp, minimum_warp])



        ax.set_box_aspect([1,(maximum_y-minimum_y)/(maximum_x-minimum_x),1])

        ax.set_xlabel("$x / m$")
        ax.set_ylabel("$y / m$")
        ax.set_zlabel("$w / m^2$")

        fig.set_figwidth(6.29921)
        fig.set_figheight(5)
        fig.set_dpi(1200)

        plt.tight_layout()
        folder_name = self.result_folder + "\\graphs" + "\\{}".format(str(self.z))

        if not os.path.exists(folder_name ):
            os.makedirs(folder_name)

        plt.savefig(folder_name+r"\plot_warping_function_z_{}.png".format(str(self.z)))
        # plt.savefig(folder_name+r"\plot_warping_function_z_{}.pgf".format(str(self.z)))



        if write_up == True:
            write_up_folder = self.result_folder.replace("shear_centre", "report\\figs")
            if not os.path.exists(write_up_folder ):
                os.makedirs(write_up_folder)
            plt.savefig(write_up_folder+r"\plot_warping_function_z_{}.png".format(str(int(self.z*100))))
            # plt.savefig(write_up_folder+r"\plot_warping_function_z_{}.pgf".format(str(int(self.z*100))))

    def warping_centre_spread(self, write_up= False):
        fig,ax = plt.subplots(1,2)

        print("entre")
        maximum_x = self.extra_df[["X0_2","X1_2","X2_2","X3_2"]].max().max()
        minimum_x = self.extra_df[["X0_2","X1_2","X2_2","X3_2"]].min().min()

        maximum_y = self.extra_df[["Y0_2","Y1_2","Y2_2","Y3_2"]].max().max()
        minimum_y = self.extra_df[["Y0_2","Y1_2","Y2_2","Y3_2"]].min().min()


        seismic = cm.get_cmap('seismic', 256)
        PiYG = cm.get_cmap('PiYG', 256)

        for index, row in self.extra_df.iterrows():
            x_wc = row["x_wc"]
            y_wc = row["y_wc"]

            centroid_x = (row["X0_2"]+row["X1_2"]+row["X2_2"]+row["X3_2"])*0.25
            centroid_y = (row["Y0_2"]+row["Y1_2"]+row["Y2_2"]+row["Y3_2"])*0.25


            def get_colour(centroid_y):
                centroid_y = centroid_y
                range_w =  maximum_y-minimum_y

                Float_between_0_and_1 = (centroid_y-minimum_y)/range_w
                return Float_between_0_and_1

            radius = np.sqrt(centroid_x**2 + centroid_y**2)



            # if centroid_x < 0.05 and abs(centroid_y)>0.36:
            #     points = [(row["X0_2"],row["Y0_2"]),(row["X1_2"],row["Y1_2"]),(row["X2_2"],row["Y2_2"]),(row["X3_2"],row["Y3_2"])]
            #     element = patch.Polygon(points, linewidth=1, edgecolor='black', facecolor="black")
            #     ax[0].add_patch(element)

            if centroid_x < -0.02:
                points = [(row["X0_2"],row["Y0_2"]),(row["X1_2"],row["Y1_2"]),(row["X2_2"],row["Y2_2"]),(row["X3_2"],row["Y3_2"])]
                element = patch.Polygon(points, linewidth=0.01, edgecolor='black', facecolor=seismic(get_colour(centroid_y)))
                ax[0].add_patch(element )
                ax[1].scatter(x_wc,y_wc, color= seismic(get_colour(centroid_y)),s = 4)



            elif centroid_x > -0.02 and centroid_x<0:
                points = [(row["X0_2"],row["Y0_2"]),(row["X1_2"],row["Y1_2"]),(row["X2_2"],row["Y2_2"]),(row["X3_2"],row["Y3_2"])]
                element = patch.Polygon(points, linewidth=0.01, edgecolor='black', facecolor=PiYG(get_colour(centroid_y)))
                ax[0].add_patch(element )
                ax[1].scatter(x_wc,y_wc, color = PiYG(get_colour(centroid_y)), s = 4)


            elif radius > 0.4:
                points = [(row["X0_2"],row["Y0_2"]),(row["X1_2"],row["Y1_2"]),(row["X2_2"],row["Y2_2"]),(row["X3_2"],row["Y3_2"])]
                element = patch.Polygon(points, linewidth=0.01, edgecolor='black', facecolor=seismic(get_colour(centroid_y)))
                ax[0].add_patch(element )
                ax[1].scatter(x_wc,y_wc, color= seismic(get_colour(centroid_y)),s = 4)

                # else:
                #     ax[1].scatter(x_wc,y_wc, color = "green")


            elif radius <0.4:
                points = [(row["X0_2"],row["Y0_2"]),(row["X1_2"],row["Y1_2"]),(row["X2_2"],row["Y2_2"]),(row["X3_2"],row["Y3_2"])]
                element = patch.Polygon(points, linewidth=0.01, edgecolor='black', facecolor=PiYG(get_colour(centroid_y)))
                ax[0].add_patch(element )
                ax[1].scatter(x_wc,y_wc, color = PiYG(get_colour(centroid_y)),s = 4)

        # Plot the mean warping centre

        MeanRCX = self.main_df["MeanRCX"][self.z]
        MeanRCY = self.main_df["MeanRCY"][self.z]
        MeanWCX = self.main_df["MeanWCX"][self.z]
        MeanWCY = self.main_df["MeanWCY"][self.z]

        ax[1].scatter(MeanRCX ,MeanRCY, marker = "x",s = 150, c="c" )
        ax[1].scatter(MeanWCX ,MeanWCY, marker = "+",s = 150, c="m")


        ax[0].set_ylim(minimum_y,maximum_y)
        ax[0].set_xlim(minimum_x,maximum_x)

        ax[0].set_xlabel("x")
        ax[0].set_ylabel("y")


        ax[1].scatter(x_wc,y_wc, color = PiYG(get_colour(centroid_y)))
        ax[1].scatter(x_wc,y_wc, color = PiYG(get_colour(centroid_y)))


        ax[1].locator_params(axis='y', nbins=5)

        ax[1].set_box_aspect(1.0)

        fig.set_figwidth(6.29921)
        fig.set_dpi(500)

        plt.tight_layout()
        folder_name = self.result_folder + "\\graphs" + "\\{}".format(str(self.z))


        if not os.path.exists(folder_name ):
            os.makedirs(folder_name)
        plt.savefig(folder_name+r"\warping_centre_spread_z_{}.png".format(str(self.z)))
        plt.savefig(folder_name+r"\warping_centre_spread_z_{}.pgf".format(str(self.z)))


        if write_up == True:
            write_up_folder = self.result_folder.replace("shear_centre", "report\\figs")
            if not os.path.exists(write_up_folder ):
                os.makedirs(write_up_folder)
            plt.savefig(write_up_folder+r"\warping_centre_spread_z_{}.png".format(str(int(self.z*100))))
            plt.savefig(write_up_folder+r"\warping_centre_spread_z_{}.pgf".format(str(int(self.z*100))))


    def warping_centre_spread2(self, write_up= False):
        fig,ax = plt.subplots(1,2)
        fig.set_dpi(1200)
        print("entre")
        maximum_x = self.extra_df[["X0_2","X1_2","X2_2","X3_2"]].max().max()
        minimum_x = self.extra_df[["X0_2","X1_2","X2_2","X3_2"]].min().min()

        maximum_y = self.extra_df[["Y0_2","Y1_2","Y2_2","Y3_2"]].max().max()
        minimum_y = self.extra_df[["Y0_2","Y1_2","Y2_2","Y3_2"]].min().min()


        seismic = cm.get_cmap('seismic', 256)
        PiYG = cm.get_cmap('PiYG', 256)

        for index, row in self.extra_df.iterrows():
            x_wc = row["x_wc"]
            y_wc = row["y_wc"]

            centroid_x = (row["X0_2"]+row["X1_2"]+row["X2_2"]+row["X3_2"])*0.25
            centroid_y = (row["Y0_2"]+row["Y1_2"]+row["Y2_2"]+row["Y3_2"])*0.25


            def get_colour(centroid_y):
                centroid_y = centroid_y
                range_w =  maximum_y-minimum_y

                Float_between_0_and_1 = (centroid_y-minimum_y)/range_w
                return Float_between_0_and_1

            radius = np.sqrt(centroid_x**2 + centroid_y**2)



            if centroid_x < 0.05 and abs(centroid_y)>0.36:
                points = [(row["X0_2"],row["Y0_2"]),(row["X1_2"],row["Y1_2"]),(row["X2_2"],row["Y2_2"]),(row["X3_2"],row["Y3_2"])]
                element = patch.Polygon(points, linewidth=1, edgecolor='black', facecolor="black")
                ax[0].add_patch(element)

            elif centroid_x < -0.02:
                points = [(row["X0_2"],row["Y0_2"]),(row["X1_2"],row["Y1_2"]),(row["X2_2"],row["Y2_2"]),(row["X3_2"],row["Y3_2"])]
                element = patch.Polygon(points, linewidth=0.01, edgecolor='black', facecolor=seismic(get_colour(centroid_y)))
                ax[0].add_patch(element )
                ax[1].scatter(x_wc,y_wc, color= seismic(get_colour(centroid_y)),s = 4)



            elif centroid_x > -0.02 and centroid_x<0:
                points = [(row["X0_2"],row["Y0_2"]),(row["X1_2"],row["Y1_2"]),(row["X2_2"],row["Y2_2"]),(row["X3_2"],row["Y3_2"])]
                element = patch.Polygon(points, linewidth=0.01, edgecolor='black', facecolor=PiYG(get_colour(centroid_y)))
                ax[0].add_patch(element )
                ax[1].scatter(x_wc,y_wc, color = PiYG(get_colour(centroid_y)), s = 4)


            elif radius > 0.4:
                points = [(row["X0_2"],row["Y0_2"]),(row["X1_2"],row["Y1_2"]),(row["X2_2"],row["Y2_2"]),(row["X3_2"],row["Y3_2"])]
                element = patch.Polygon(points, linewidth=0.01, edgecolor='black', facecolor=seismic(get_colour(centroid_y)))
                ax[0].add_patch(element )
                ax[1].scatter(x_wc,y_wc, color= seismic(get_colour(centroid_y)),s = 4)

                # else:
                #     ax[1].scatter(x_wc,y_wc, color = "green")


            elif radius <0.4:
                points = [(row["X0_2"],row["Y0_2"]),(row["X1_2"],row["Y1_2"]),(row["X2_2"],row["Y2_2"]),(row["X3_2"],row["Y3_2"])]
                element = patch.Polygon(points, linewidth=0.01, edgecolor='black', facecolor=PiYG(get_colour(centroid_y)))
                ax[0].add_patch(element )
                ax[1].scatter(x_wc,y_wc, color = PiYG(get_colour(centroid_y)),s = 4)

        # Plot the mean warping centre

        MeanRCX = self.main_df["MeanRCX"][self.z]
        MeanRCY = self.main_df["MeanRCY"][self.z]
        MeanWCX = self.main_df["MeanWCX"][self.z]
        MeanWCY = self.main_df["MeanWCY"][self.z]

        ax[1].scatter(MeanRCX ,MeanRCY, marker = "x",s = 150, c="c" )
        ax[1].scatter(MeanWCX ,MeanWCY, marker = "+",s = 150, c="m")


        ax[0].set_ylim(minimum_y,maximum_y)
        ax[0].set_xlim(minimum_x,maximum_x)

        ax[0].set_xlabel("x")
        ax[0].set_ylabel("y")


        ax[1].scatter(x_wc,y_wc, color = PiYG(get_colour(centroid_y)))
        ax[1].scatter(x_wc,y_wc, color = PiYG(get_colour(centroid_y)))


        ax[1].locator_params(axis='y', nbins=5)

        ax[1].set_box_aspect(1.0)

        fig.set_figwidth(6.29921)
        fig.set_figheight(5)
        fig.set_dpi(1200)

        plt.tight_layout()
        folder_name = self.result_folder + "\\graphs" + "\\{}".format(str(self.z))


        if not os.path.exists(folder_name ):
            os.makedirs(folder_name)
        plt.savefig(folder_name+r"\warping_centre_spread_z_{}.png".format(str(self.z)))
        # plt.savefig(folder_name+r"\warping_centre_spread_z_{}.pgf".format(str(self.z)))


        if write_up == True:
            write_up_folder = self.result_folder.replace("shear_centre", "report\\figs")
            if not os.path.exists(write_up_folder ):
                os.makedirs(write_up_folder)
            plt.savefig(write_up_folder+r"\warping_centre_spread_z_{}.png".format(str(int(self.z*100))))
            # plt.savefig(write_up_folder+r"\warping_centre_spread_z_{}.pgf".format(str(int(self.z*100))))


    def warping_centre_line(self, write_up= False):
        print(len(self.extra_df["X0_0"]))
        w_array = np.zeros([33,20])


        # n=0
        # for i in range(35):
        #     k = 0
        #     for index, row in self.extra_df.iterrows():
        #         centroid_x = (row["X0_2"]+row["X1_2"]+row["X2_2"]+row["X3_2"])*0.25
        #         centroid_y = (row["Y0_2"]+row["Y1_2"]+row["Y2_2"]+row["Y3_2"])*0.25

        #         angle = np.arctan(centroid_y/centroid_x)
        #         radius = np.sqrt(centroid_x**2 +  centroid_y**2)



        #         if angle>0:

        #             angle_bin = int(angle/(np.pi/66))
        #             if angle_bin == i:
        #                 k+=1
        #                 n+=1


        for index, row in self.extra_df.iterrows():
            centroid_x = (row["X0_2"]+row["X1_2"]+row["X2_2"]+row["X3_2"])*0.25
            centroid_y = (row["Y0_2"]+row["Y1_2"]+row["Y2_2"]+row["Y3_2"])*0.25

            angle = np.arctan(centroid_y/centroid_x)
            radius = np.sqrt(centroid_x**2 +  centroid_y**2)-0.38

            W = (row["W0"] + row["W1"] + row["W2"] + row["W3"])/4


            if angle>0:
                angle_bin = int(angle/(np.pi/66))
                radius_bin = int(radius/0.002)
                assert w_array[angle_bin][radius_bin] == 0
                w_array[angle_bin][radius_bin] = W



        w_mean = np.mean(w_array, axis = 1).reshape(-1, 1)



        print(w_mean)

        w_noramlised = w_array - w_mean
        x = np.arange(20)
        y = w_noramlised[30]

        print(w_noramlised)

        plt.plot(x,y)

        plt.show()

        print(w_array)

    def get_J(self):
        # maximum_warp = 1000*self.main_df["MaxWarp"][self.z]
        # minimum_warp = 1000*self.main_df["MinWarp"][self.z]

        # maximum_x = self.extra_df["X0_0"].max()
        # minimum_x = self.extra_df["X0_0"].min()

        # maximum_y = self.extra_df["Y0_0"].max()
        # minimum_y = self.extra_df["Y0_0"].min()
        J1 = 0.0
        J2 = 0.0
        J3 = 0.0
        J4 = 0.0
        for index, row in self.extra_df.iterrows():
            X2 = [row["X0_2"],row["X1_2"],row["X2_2"],row["X3_2"]]
            Y2 = [row["Y0_2"],row["Y1_2"],row["Y2_2"],row["Y3_2"]]
            dArea = Polygon(zip(X2, Y2)).area
            X2_centroid = np.mean(X2)
            Y2_centroid = np.mean(Y2)
            integral1 = (X2_centroid-row["x_rc"])**2
            integral2 = (Y2_centroid-row["y_rc"])**2
            integral3 = (X2_centroid-row["x_rc"])*(X2_centroid-row["x_wc"])
            integral4 = (Y2_centroid-row["y_rc"])*(Y2_centroid-row["y_wc"])
            # integral1 = (row["x_rc"]-row["x_wc"])**2
            # integral2 = (row["y_rc"]-row["y_wc"])**2


            #+(Y2_centroid-row["y_rc"])**2+(X2_centroid-row["x_rc"])*(X2_centroid-row["x_wc"])-(Y2_centroid-row["y_rc"])*(Y2_centroid-row["y_wc"])
            J1 += integral1*dArea
            J2 += integral2*dArea
            J3 += integral3*dArea
            J4 += integral4*dArea
        return J1-J3+J2-J4

    def plot_deflected_section(self,name=" "):
        fig,ax = plt.subplots(2,1)
        for index, row in self.extra_df.iterrows():
            ax[0].plot(np.array([row["X0_0"],row["X1_0"],row["X2_0"],row["X3_0"],row["X0_0"]]),np.array([row["Y0_0"],row["Y1_0"],row["Y2_0"],row["Y3_0"],row["Y0_0"]]), c = (0.1,0.1,0.1, 0.5))
            Af = 2000
            dX0 = (row["X0_1"]-row["X0_0"])*Af
            dX1 = (row["X1_1"]-row["X1_0"])*Af
            dX2 = (row["X2_1"]-row["X2_0"])*Af
            dX3 = (row["X3_1"]-row["X3_0"])*Af

            dY0 = (row["Y0_1"]-row["Y0_0"])*Af
            dY1 = (row["Y1_1"]-row["Y1_0"])*Af
            dY2 = (row["Y2_1"]-row["Y2_0"])*Af
            dY3 = (row["Y3_1"]-row["Y3_0"])*Af


            points = [(row["X0_0"],row["Y0_0"]),(row["X1_0"],row["Y1_0"]),(row["X2_0"],row["Y2_0"]),(row["X3_0"],row["Y3_0"])]
            element = patch.Polygon(points, facecolor="lightgrey", zorder=1)
            ax[0].add_patch(element)
            points = [(row["X0_0"],row["Y0_0"]),(row["X1_0"],row["Y1_0"]),(row["X2_0"],row["Y2_0"]),(row["X3_0"],row["Y3_0"])]
            element = patch.Polygon(points, facecolor="lightslategrey")

            ax[1].add_patch(element)




            points = [(row["X0_0"]+dX0,row["Y0_0"]+dY0),(row["X1_0"]+dX1,row["Y1_0"]+dY1),(row["X2_0"]+dX2,row["Y2_0"]+dY2),(row["X3_0"]+dX3,row["Y3_0"]+dY3)]
            element = patch.Polygon(points, facecolor="red", zorder=2)
            ax[0].add_patch(element)

            #ax[0].plot(np.array([row["X0_0"]+dX0,row["X1_0"]+dX1,row["X2_0"]+dX2,row["X3_0"]+dX3,row["X0_0"]+dX0]),np.array([row["Y0_0"]+dY0,row["Y1_0"]+dY1,row["Y2_0"]+dY2,row["Y3_0"]+dY3,row["Y0_0"]+dY0]), c = (0.5,0.1,0.1, 0.5))

            # ax[1].plot(np.array([row["X0_0"],row["X1_0"],row["X2_0"],row["X3_0"],row["X0_0"]]),np.array([row["Y0_0"],row["Y1_0"],row["Y2_0"],row["Y3_0"],row["Y0_0"]]), c = (0.1,0.1,0.1, 0.5))

            x_centroid = (row["X0_0"]+row["X1_0"]+row["X2_0"]+row["X3_0"])/4
            y_centroid = (row["Y0_0"]+row["Y1_0"]+row["Y2_0"]+row["Y3_0"])/4

            x_rc = row["x_rc"]
            y_rc = row["y_rc"]

            def get_colour(x_centroid,y_centroid ):
                sin = np.sin(y_centroid/(x_centroid**2+y_centroid**2)**0.5)
                sin = (sin+1)/2
                return sin

            seismic = cm.get_cmap('Set1', 256)

            ax[1].plot([x_rc, x_centroid],[y_rc, y_centroid], color= seismic(get_colour(x_centroid,y_centroid)))


            # avaerage warping as a number from 1 to 256








            #ax.plot_surface(np.array([[row["X0_2"],row["X1_2"]],[row["X3_2"],row["X2_2"]]]),np.array([[row["Y0_2"],row["Y1_2"]],[row["Y3_2"],row["Y2_2"]]]), 1000*np.array([[row["W0"],row["W1"]],[row["W3"],row["W2"]]]),vmin=minimum_warp, vmax=maximum_warp, rstride=1, cstride=1, cmap=cm.plasma,linewidth=0.1, antialiased=False, edgecolor=(0.1,0.1,0.1,0.5))

            #need to get the colour for the contour plot

            # cmap = cf.get_cmap()


            # seismic = cm.get_cmap('seismic', 256)
            # # avaerage warping as a number from 1 to 256


            # def get_colour():
            #     mean_warp = 1000*(row["W0"]+row["W1"]+row["W2"]+row["W2"])/4
            #     range_w =  maximum_warp-minimum_warp
            #     Float_between_0_and_1 = (mean_warp-minimum_warp)/range_w
            #     return Float_between_0_and_1


            # z_offset = minimum_warp - 0.2*(maximum_warp-minimum_warp)

            # ax.plot_surface(np.array([[row["X0_2"],row["X1_2"]],[row["X3_2"],row["X2_2"]]]),np.array([[row["Y0_2"],row["Y1_2"]],[row["Y3_2"],row["Y2_2"]]]), np.array([[z_offset,z_offset],[z_offset,z_offset]]), color = seismic(get_colour()), shade=False)
            # y_offset = maximum_y + 0.2*(maximum_y-minimum_y)
            # ax.plot_surface(np.array([[row["X0_2"],row["X1_2"]],[row["X3_2"],row["X2_2"]]]),np.array([[y_offset,y_offset],[y_offset,y_offset]]), 1000*np.array([[row["W0"],row["W1"]],[row["W3"],row["W2"]]]), color = seismic(get_colour()),shade=False)
            # x_offset = minimum_x - 0.2*(maximum_x-minimum_x)

            # ax.plot_surface(np.array([[x_offset ,x_offset ],[x_offset , x_offset]]),np.array([[row["Y0_2"],row["Y1_2"]],[row["Y3_2"],row["Y2_2"]]]), 1000*np.array([[row["W0"],row["W1"]],[row["W3"],row["W2"]]]), color = seismic(get_colour()), shade=False)
        ax[0].set_aspect('equal', adjustable='box')
        # ax[1].set_aspect('equal', adjustable='box')
        plt.tight_layout()
        fig.set_figwidth(6.29921/2)
        fig.set_figheight(5.0)
        fig.set_dpi(300)
        plt.tight_layout()

        folder_name = r"D:\\report\\figs"+r"\\"+"NACA"+ r"\graph_hodograph"

        if not os.path.exists(folder_name ):
            os.makedirs(folder_name)


        plt.savefig(folder_name+r"\graph_{}.png".format(name))
        plt.savefig(folder_name+r"\graph_{}.pgf".format(name))


    def plot_deflected_section2(self,name=" "):
        fig,ax = plt.subplots()
        n=0
        for index, row in self.extra_df.iterrows():
            # ax.plot(np.array([row["X0_0"],row["X1_0"],row["X2_0"],row["X3_0"],row["X0_0"]]),np.array([row["Y0_0"],row["Y1_0"],row["Y2_0"],row["Y3_0"],row["Y0_0"]]), c = (1,0.1,0.1, 1))
            ax.plot(np.array([row["X0_0"],row["X1_0"],row["X2_0"],row["X3_0"],row["X0_0"]]),np.array([row["Y0_0"],row["Y1_0"],row["Y2_0"],row["Y3_0"],row["Y0_0"]]), c = (0.1,0.1,0.1, 0.5), zorder=0)


            # Af = 2000
            # dX0 = (row["X0_1"]-row["X0_0"])*Af
            # dX1 = (row["X1_1"]-row["X1_0"])*Af
            # dX2 = (row["X2_1"]-row["X2_0"])*Af
            # dX3 = (row["X3_1"]-row["X3_0"])*Af

            # dY0 = (row["Y0_1"]-row["Y0_0"])*Af
            # dY1 = (row["Y1_1"]-row["Y1_0"])*Af
            # dY2 = (row["Y2_1"]-row["Y2_0"])*Af
            # dY3 = (row["Y3_1"]-row["Y3_0"])*Af


            # points = [(row["X0_0"],row["Y0_0"]),(row["X1_0"],row["Y1_0"]),(row["X2_0"],row["Y2_0"]),(row["X3_0"],row["Y3_0"])]
            # element = patch.Polygon(points, facecolor="lightgrey", zorder=1)
            # ax[0].add_patch(element)
            # points = [(row["X0_0"],row["Y0_0"]),(row["X1_0"],row["Y1_0"]),(row["X2_0"],row["Y2_0"]),(row["X3_0"],row["Y3_0"])]
            # element = patch.Polygon(points, facecolor="lightslategrey")

            # ax[1].add_patch(element)

            # points = [(row["X0_0"]+dX0,row["Y0_0"]+dY0),(row["X1_0"]+dX1,row["Y1_0"]+dY1),(row["X2_0"]+dX2,row["Y2_0"]+dY2),(row["X3_0"]+dX3,row["Y3_0"]+dY3)]
            # element = patch.Polygon(points, facecolor="red", zorder=2)
            # ax[0].add_patch(element)

            x_centroid = (row["X0_0"]+row["X1_0"]+row["X2_0"]+row["X3_0"])/4
            y_centroid = (row["Y0_0"]+row["Y1_0"]+row["Y2_0"]+row["Y3_0"])/4

            x_rc = row["x_rc"]
            y_rc = row["y_rc"]
            # ax.plot([x_rc, x_centroid],[y_rc, y_centroid], color= "tab:purple")


            def get_colour(x_centroid,y_centroid ):
                sin = np.sin(y_centroid/(x_centroid**2+y_centroid**2)**0.5)
                sin = (sin+1)/2
                return sin

            seismic = cm.get_cmap('Set1', 256)

            # ax.plot([x_rc, x_centroid],[y_rc, y_centroid], color= "tab:purple", zorder=0)
            ax.scatter([x_rc,y_rc], color= "tab:purple", zorder=1)

            n+=1

        MeanRCX = self.main_df["MeanRCX"][self.z]
        MeanRCY = self.main_df["MeanRCY"][self.z]
        ax.scatter(MeanRCX,MeanRCY,color= "tab:green", marker="X",s=150, zorder=2)
        ax.set_aspect('equal', adjustable='box')
        plt.tight_layout()
        fig.set_figwidth(6.29921/2)
        fig.set_figheight(5.0)
        plt.tight_layout()

        folder_name = r"D:\\report\\figs"+r"\\"+"D"+ r"\graph_hodograph"

        if not os.path.exists(folder_name ):
            os.makedirs(folder_name)


        plt.savefig(folder_name+r"\graph_{}.png".format(name))
        plt.savefig(folder_name+r"\graph_{}.pgf".format(name))






class Beam(Result_Data):
    def __init__(self,main_df,z, analyis_folder):
        self.analyis_folder = analyis_folder
        Result_Data.__init__(self, self.analyis_folder)
        self.main_df = main_df
        self.z = z

    def _navigate(self, analysis_arguments, chdir = False ):
        root = self.analyis_folder
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


    def _make_string_windows_compatible(self, string1):
        string1 = string1.replace(", ", "_")
        string1 = string1.replace("[", "")
        string1 = string1.replace("]", "")
        return string1



    def z_rotation_along_beam(self):
        z = self.main_df.index.values.tolist()
        theta_z = self.main_df["GlobalRotationVectorZ"].values*180/np.pi
        return z, theta_z

    def warping_magnitude_along_beam(self):
        z = self.main_df.index.values.tolist()
        w = self.main_df["WarpingMagnitude"].values
        return z, w

    def twist_along_beam(self):
        z = self.main_df.index.values.tolist()

        twist =  self.main_df["Twist"].values
        return z, twist

    def gamma_along_beam(self):
        z = self.main_df.index.values.tolist()
        w = self.main_df["WarpingMagnitude"].values**2
        w = w*self.main_df["Area"].values
        twist =  self.main_df["Twist"].values**2
        return z, w/twist
    def stress_magnitude_along_beam(self):
        z = self.main_df.index.values.tolist()
        w = self.main_df["StressMagnitude"].values
        return z, w
    def MeanRCX_along_beam(self):
        z = self.main_df.index.values.tolist()
        w = self.main_df["MeanRCX"].values
        return z, w

    # def _get_rate_of_distortion(self, z):
    #     z_list = self.main_df.index.values.tolist()
    #     ResultSection=z_list.index(z)
    #     if ResultSection==0:
    #         d_theta = abs(self.main_df["SpreadRC"][z_list[ResultSection]] - self.main_df["SpreadRC"][z_list[ResultSection+1]])
    #         dz = 0.05
    #         dtheta_dz = d_theta/dz
    #     elif ResultSection == len(self.list_of_z_values)-3:
    #         d_theta = abs(self.main_df["SpreadRC"][z_list[ResultSection-1]] - self.main_df["SpreadRC"][z_list[ResultSection]])
    #         dz = 0.05
    #         dtheta_dz = d_theta/dz
    #     elif ResultSection > len(self.list_of_z_values)-3:
    #         pass
    #     else:
    #         print(ResultSection)
    #         d_theta = abs(self.main_df["SpreadRC"][z_list[ResultSection-1]] - self.main_df["SpreadRC"][z_list[ResultSection+1]])
    #         dz = 0.1
    #         dtheta_dz = d_theta/dz
    #     # remove floating point error
    #     significant_digits = 10
    #     Twist =  round(dtheta_dz, significant_digits - int(math.floor(math.log10(abs(dtheta_dz)))) - 1)
    #     return Twist







    def distorsion_along_beam(self, LoadSection):
        loading_z = self.main_df.index.values.tolist()[LoadSection]
        z_list = self.main_df.index.values.tolist()

        folder_name =  self._navigate(["..","..", "LSC_torque"], chdir = True)
        LSC_csv =r"\LSC.csv"

        # if not os.path.exists(extra_information_csv):
        #     #create the csv
        #     column_names =  []
        #     extra_df = pd.DataFrame(columns=column_names)
        #     extra_df.index.name = "e"
        # else:
        #     extra_df = pd.read_csv(extra_information_csv, header = 0, index_col = 0)
        # extra_df = extra_df.astype(np.float64)

        if not os.path.exists(folder_name + LSC_csv):
            column_names =  []
            LSC_df = pd.DataFrame(columns=column_names)
            LSC_df.index.name = "z"
        else:
            LSC_df = pd.read_csv(folder_name + LSC_csv, header = 0, index_col = 0)
        LSC_df = LSC_df.astype(np.float64)

        above = 0.0
        bellow = 0.0
        # above_counter = 0
        # bellow_counter = 0
        print(LSC_df.index)

        if loading_z not in LSC_df.index:
            for z in z_list:
                if z >= loading_z:
                    # above += self._get_rate_of_distortion(z)
                    above += self.main_df["SpreadRC"][z]
                elif z < loading_z:
                    bellow += self.main_df["SpreadRC"][z]
                # else:
                #     print("z = ", z )
            data = {"above":above, "bellow":bellow, "MeanRCX":self.main_df["MeanRCX"][loading_z]}
            dfr = pd.DataFrame(data = data, index = [loading_z])
            dfr.index.name = "z"
            LSC_df =  LSC_df.append(dfr, ignore_index = False)
            LSC_df.to_csv(folder_name + LSC_csv)
        return LSC_df












