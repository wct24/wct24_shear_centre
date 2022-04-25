import subprocess
import smtplib, ssl
import pandas as pd
import os
import time
import numpy as np
from transforms3d.euler import mat2euler
import math
import matplotlib.pyplot as plt
from matplotlib import cm
from decimal import Decimal
from shapely.geometry import Polygon



class Result_Data:
    def __init__(self, analysis_folder):
        self.analysis_folder = analysis_folder
        self.beam_csv = analysis_folder + r"\beam.csv"
        self.beam_df = pd.read_csv(self.beam_csv, header = 0,index_col=0)
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
        s = pd.read_csv(csv_filename, header = 0, usecols = [4,5,6,7,8])
        s.columns=["Element", "Node","x", "y" ,"z"]
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
            xy = np.array(list(zip(x,y)))
            xSorted = xy[xy[:, 0].argsort()]
            y_sorted = xy[xy[:, 1].argsort()]
            leftMost = xSorted[:2, :]
            rightMost = xSorted[2:, :]

            leftMost = leftMost[leftMost[:, 1].argsort()]
            (tl, bl) = leftMost

            rightMost = rightMost[rightMost[:, 1].argsort()]
            (tr, br) = rightMost
            # element = order_points(element)
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

    def section_warping_magnitude(self, ResultSection):
           # get the z coordinates of the sections
        # get the z coordinates of the sections
        section_warping_magnitude_csv = self.result_folder+ r"\section_warping_magnitude.csv"
        if not os.path.exists(section_warping_magnitude_csv):
            #create the csv
            column_names =  ["Warping Magnitude"]
            wm_df = pd.DataFrame(columns=column_names)
            wm_df.index.name = "z"
        else:
            wm_df = pd.read_csv(section_warping_magnitude_csv, header = 0, index_col = 0)
        wm_df = wm_df.astype(np.float64)

        z = self.list_of_z_values[ResultSection]

        if z not in wm_df.index:
            df1 = self.U_df.loc[self.U_df["z"]==z]
            element_array = self._element_list(z)

            # the element will appear twice once downbeam and once up beam for a 3D element
            element_array = np.unique(element_array)
            df1 = df1.reset_index()
            maximum_warp = df1["U3"].max()
            minimum_warp = df1["U3"].min()
            x_0 = df1["x"].values
            y_0 = df1["y"].values
            z_0 = df1["z"].values
            # plt.scatter(x_0[1:100], y_0[1:100], z_0[1:100])
            warping_displacement = df1["U3"].values

            # find the rotation:
            x_1 = x_0 + df1["U1"].values
            y_1 = y_0 + df1["U2"].values
            z_1 = z_0 + df1["U3"].values

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
            U, S, Vt = np.linalg.svd(H)
            R = Vt.T @ U.T

            t = -R @ centroid_A + centroid_B
            XYZ_2  = R @ A + t

            x_2 = XYZ_2[0]
            y_2 = XYZ_2[1]
            w = XYZ_2[2]-z_0


            warping_magnitude = 0.0
            A = 0.0

            for i in range(np.shape(element_array)[0]):
                (X0_0,Y0_0,X1_0,Y1_0, X2_0,Y2_0, X3_0,Y3_0) = element_array[i]
                AFxy = 1
                AFz  = 1
                condition = (df1['x'] == X0_0) & (df1['y'] == Y0_0)
                b = df1.index[condition].tolist()

                X0_1 = x_2[b[0]]
                Y0_1 = y_2[b[0]]
                W0 = w[b[0]]


                condition = (df1['x'] == X1_0) & (df1['y'] == Y1_0)
                b = df1.index[condition].tolist()
                X1_1 = x_2[b[0]]
                Y1_1 = y_2[b[0]]
                W1 = w[b[0]]

                condition = (df1['x'] == X2_0) & (df1['y'] == Y2_0)
                b = df1.index[condition].tolist()
                X2_1 = x_2[b[0]]
                Y2_1 = y_2[b[0]]
                W2 = w[b[0]]


                condition = (df1['x'] == X3_0) & (df1['y'] == Y3_0)
                b = df1.index[condition].tolist()
                X3_1 = x_2[b[0]]
                Y3_1 = y_2[b[0]]
                W3 = w[b[0]]


                #find the volume of an 8 point pryzm []
                w_mean = (W0+W1+W2+W3)/4
                #shoelace formula


                x = [X0_1, X1_1, X2_1, X3_1]
                y = [Y0_1, Y1_1, Y2_1, Y3_1]
                dA = Polygon(zip(x, y)).area # Assuming the OP's x,y coordinates
                warping_magnitude += w_mean**2*dA
                A += dA
            dfr = pd.DataFrame(data = {"Warping Magnitude":[warping_magnitude]}, index = [z])
            dfr.index.name = "z"
            wm_df = wm_df.append(dfr, ignore_index = False)
            wm_df.to_csv(section_warping_magnitude_csv)
        warping_magnitude = wm_df.loc[z,"Warping Magnitude"]
        # print(A)
        return warping_magnitude

    def warping_magnitude_along_beam(self):
        rotationz_list =[]
        for i in range(len(self.list_of_z_values)):
            rotationz_list.append(self.section_warping_magnitude(i))
        z_list = self.list_of_z_values
        # ax.plot(z_list, rotation_z_list, label="$S_x({},{},{})$".format(self.beam_df["LoadX"][0],self.beam_df["LoadY"][0],z_list[int(self.beam_df["LoadZ"][0])]))
        return z_list, rotationz_list

    def plot_deformed_cross_section_3D(self,LoadZ):
        # get the z coordinates of the sections
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        # get the z coordinates of the sections
        z = self.list_of_z_values[LoadZ]

        df1 = self.U_df.loc[self.U_df["z"]==z]
        element_array = self._element_list(z)
        df1 = df1.reset_index()



        maximum_warp = df1["U3"].max()
        minimum_warp = df1["U3"].min()
        x_0 = df1["x"].values
        y_0 = df1["y"].values
        z_0 = df1["z"].values
        # plt.scatter(x_0[1:100], y_0[1:100], z_0[1:100])
        warping_displacement = df1["U3"].values

        # find the rotation:
        x_1 = x_0 + df1["U1"].values
        y_1 = y_0 + df1["U2"].values
        z_1 = z_0 + df1["U3"].values

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
        U, S, Vt = np.linalg.svd(H)
        R = Vt.T @ U.T

        t = -R @ centroid_A + centroid_B
        XYZ_2  = R @ A + t

        x_2 = XYZ_2[0]
        y_2 = XYZ_2[1]
        w = XYZ_2[2]-z_0


        for i in range(np.shape(element_array)[0]):
            [X0_0,Y0_0,X1_0,Y1_0, X2_0,Y2_0, X3_0,Y3_0] = element_array[i]
            AFxy = 1
            AFz  = 1
            condition = (df1['x'] == X0_0) & (df1['y'] == Y0_0)
            b = df1.index[condition].tolist()
            X0_1 = x_2[b[0]]
            Y0_1 = y_2[b[0]]
            W0 = w[b[0]]
            condition = (df1['x'] == X1_0) & (df1['y'] == Y1_0)
            b = df1.index[condition].tolist()
            X1_1 = x_2[b[0]]
            Y1_1 = y_2[b[0]]
            W1 = w[b[0]]

            condition = (df1['x'] == X2_0) & (df1['y'] == Y2_0)
            b = df1.index[condition].tolist()
            X2_1 = x_2[b[0]]
            Y2_1 = y_2[b[0]]
            W2 = w[b[0]]

            condition = (df1['x'] == X3_0) & (df1['y'] == Y3_0)
            b = df1.index[condition].tolist()
            X3_1 = x_2[b[0]]
            Y3_1 = y_2[b[0]]
            W3 = w[b[0]]

            ax.plot_surface(np.array([[X0_0,X1_0],[X3_0,X2_0]]),np.array([[Y0_0,Y1_0],[Y3_0,Y2_0]]), np.array([[0.0,0.0],[0.0,0.0]]), color = (0.1,0.1,0.1, 0.5))
            ax.plot_surface(np.array([[X0_1,X1_1],[X3_1,X2_1]]),np.array([[Y0_1,Y1_1],[Y3_1,Y2_1]]), np.array([[W0,W1],[W3,W2]]),vmin=minimum_warp, vmax=maximum_warp, rstride=1, cstride=1, cmap=cm.seismic,linewidth=0.3, antialiased=False, edgecolor=(0,0,0,1))
        fig.suptitle("Deflection".format(z))
        plt.show()

    def magnitude_of_w(self):
        return 0

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
        script = r"C:\Users\touze\project\wct24_shear_centre\abaqus_scripts\shape_{}.py".format(self.ShapeId)
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


    def SimpleShearLoad(self, LoadZ, LoadX, LoadY=0.0, LoadMagnitude = -10):
        # print(AnalysisType)
        # print(LoadX)
        assert LoadZ < self.length*20, "LoadZ is outside the length of beam"
        assert type(LoadZ) == int, "LoadZ is a position, beam is split into 0.05m segments"

        AnalysisType = "1. Simple_Shear_Load"
        folder_name = self._navigate([AnalysisType, "Beam_Repository", LoadMagnitude, LoadZ, LoadX], chdir = True)
        # print(os.path.exists(folder_name + r"\displacement.csv"))
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
            # self._run_script()
        else:
            pass
        return Result_Data(folder_name) #+r'\beam.csv',folder_name + r"\displacement.csv", folder_name + r"\stress.csv")

    def SimpleTorqueLoad(self, LoadZ, LoadX, LoadY=0.0, LoadMagnitude = 10, AnalysisType = "4. Simple_Torque_Load"):
        # print(AnalysisType)
        # print(LoadX)
        assert LoadZ < self.length*20, "LoadZ is outside the length of beam"
        assert type(LoadZ) == int, "LoadZ is a position, beam is split into 0.05m segments"

        folder_name = self._navigate([AnalysisType,"Beam_Repository", LoadZ, LoadX], chdir = True)

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

    def TSC(self, LoadZ, tol = 1e-5):
        """ Newton-Raphson method to find the TSC
            a small load is used to make linear"""

        #load x means the x coordinate of the load
        LoadX= 0.0 #start point

        LoadX_UB = LoadX+tol
        LoadX_LB = LoadX-tol
        Rotationz_UB = -1
        Rotationz_LB = -1

        while Rotationz_UB*Rotationz_LB > 0:
            LoadMagnitude = -1
            self.SimpleShearLoad(LoadZ, LoadX_UB, LoadMagnitude = LoadMagnitude)
            self.SimpleShearLoad(LoadZ, LoadX_LB, LoadMagnitude = LoadMagnitude)
            LoadX_UB_directory = self._navigate(["1. Simple_Shear_Load", LoadMagnitude, LoadZ, LoadX_UB])
            LoadX_LB_directory = self._navigate(["1. Simple_Shear_Load", LoadMagnitude, LoadZ, LoadX_LB])

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
            print(Rotationz_UB, Rotationz_LB )

        return LoadX

    def LSC(self, LoadZ, tol = 1e-5):
        """ Newton-Raphson method to find the TSC
            a small load is used to make linear"""
        # AnalysisType = "3. Find_LSC"

        #load x means the x coordinate of the load
        LoadX= 0.0 #start point

        LoadX_UB = LoadX+tol
        LoadX_LB = LoadX-tol
        Rotationz_UB = -1
        Rotationz_LB = -1

        while Rotationz_UB*Rotationz_LB > 0:
            LoadMagnitude = -1
            self.SimpleShearLoad(LoadZ, LoadX_UB, LoadMagnitude = LoadMagnitude)
            self.SimpleShearLoad(LoadZ, LoadX_LB, LoadMagnitude = LoadMagnitude)
            LoadX_UB_directory = self._navigate(["1. Simple_Shear_Load", LoadMagnitude, LoadZ, LoadX_UB])
            LoadX_LB_directory = self._navigate(["1. Simple_Shear_Load", LoadMagnitude, LoadZ, LoadX_LB])

            Rotationz_UB = self.Rotationz_at_z(int(LoadZ),LoadX_UB_directory + r"\displacement.csv")
            Rotationz_LB = self.Rotationz_at_z(int(LoadZ),LoadX_LB_directory + r"\displacement.csv")

            print(Rotationz_UB, Rotationz_LB )
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

    def end_rotation_x_sweep(self, start, stop, LoadZ, LoadMagnitude):
        result_folder = self._navigate(["1. Simple_Shear_Load", "Processed_Results","sweep"])
        sweep_csv = result_folder+ r"\end_rotation_x_sweep_{}_{}_{}_{}.csv".format(start,stop,LoadZ,LoadMagnitude)
        if not os.path.exists(sweep_csv):
            #create the csv
            column_names =  ["Rotation", "Warping Magnitude"]
            sweep_df = pd.DataFrame(columns=column_names)
            sweep_df.index.name = "x"
        else:
            sweep_df = pd.read_csv(sweep_csv, header = 0, index_col = 0)
        sweep_df = sweep_df.astype(np.float64)

        folder = self._navigate(["1. Simple_Shear_Load", "Beam_Repository",LoadMagnitude, LoadZ])
        # print(folder)
        # os.chdir(folder)
        # print(os.listdir(folder))

        x_list = sorted([float(name) for name in os.listdir(folder)])

        for i in range(len(x_list)):
            if x_list[i] not in sweep_df.index:
                result = self.SimpleShearLoad(LoadZ, x_list[i], LoadY=0.0, LoadMagnitude = LoadMagnitude)
                rotation = result.section_rotationz(LoadZ)
                warping  = result.section_warping_magnitude(LoadZ)
                dfr = pd.DataFrame(data = {"Rotation":[rotation*180/np.pi],"Warping Magnitude":[warping]}, index = [x_list[i]])
                dfr.index.name = "x"
                sweep_df = sweep_df.append(dfr, ignore_index = False)
                print(sweep_df)
                sweep_df.to_csv(sweep_csv)
            else:
                pass
        return sweep_df.index, sweep_df["Rotation"].values, sweep_df["Warping Magnitude"].values









#### what's important is the location of the input csv
# beam_name = r"D:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\210.0_81.0_0.3\warping"
# input_csv = Beam_name + "input.csv"

# Encastre = Beam(r"D:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\210.0_81.0_0.3\encastre")
# Warping = Beam(r"D:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\210.0_81.0_0.3\Warping")






# fig, ax = plt.subplots()
# print(Encatre.SimpleShearLoad(0,1.0).plot_z_rotation_along_beam())
# print(Warping.SimpleShearLoad(0,1.0).plot_z_rotation_along_beam())
# plt.ylim(bottom=0)
# plt.xlim(left=0)
# ax.legend()
# ax.xaxis.tick_bottom()
# plt.xlabel(r'$z / m$ ', )
# plt.ylabel(r'$\theta_{z}$ / \textdegree ')
# plt.tight_layout()
# plt.grid()
# plt.show()



# Warping.TSC_every_n_m(0.5)
# Encastre.LSC_every_n_m(0.5)
# # print("hello")
# # sc.LSC_every_n_m(0.5)
# #print(sc.SimpleShearLoad(89,1.0).plot_z_rotation_along_beam())






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




