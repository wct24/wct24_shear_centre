 def GetAll(self, ResultSection):
           # get the z coordinates of the sections
        # get the z coordinates of the sections
        z = self.list_of_z_values[ResultSection]
        main_information_csv  = self.result_folder+ "\\main_information.csv"
        extra_information_csv = self.result_folder+ "\\extra_information"+ "\\{}.csv".format(str(z))

        if not os.path.exists(main_information_csv):
            #create the csv
            column_names =  ["GlobalDisplacementVector","GlobalRotationVector","WarpingMagnitude", "StressMagnitude", "MeanRC", "SpreadRC", "MeanWC", "SpreadWC","MeanSC","SpreadSC"]
            main_df = pd.DataFrame(columns=column_names)
            main_df.index.name = "z"
            os.mkdir(self.result_folder+ "\\extra_information")


        else:
            main_df = pd.read_csv(main_information_csv, header = 0, index_col = 0)

        main_df = main_df.astype(np.float64)

        if not os.path.exists(extra_information_csv):
            #create the csv
            column_names =  ["X0_0", "Y0_0", "X1_0", "Y1_0", "X2_0", "Y2_0", "X3_0", "Y3_0", "X0_1", "Y0_1", "X1_1", "Y1_1", "X2_1", "Y2_1", "X3_1", "Y3_1", "X0_2", "Y0_2", "X1_2", "Y1_2", "X2_2", "Y2_2", "X3_2", "Y3_2","W0", "W1", "W2", "W3", "S0", "S1", "S2", "S3","x_wc","y_wc","x_sc", "y_sc", "x_rc", "y_rc"]
            extra_df = pd.DataFrame(columns=column_names)
            extra_df.index.name = "e"
        else:
            extra_df = pd.read_csv(extra_information_csv, header = 0, index_col = 0)
        extra_df = extra_df.astype(np.float64)

        # only runs if it hasn't run before
        if z not in main_df.index:
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

            GlobalDisplacementVector = centroid_B - centroid_A

            # subtract mean
            Am = A - centroid_A
            Bm = B - centroid_B

            H = Am @ np.transpose(Bm)
            U, S, Vt = np.linalg.svd(H)
            R = Vt.T @ U.T
            GlobalRotationVector = mat2euler(R, axes='sxyz')


            t = -R @ centroid_A + centroid_B
            XYZ_2  = R @ A + t

            x_2 = XYZ_2[0]
            y_2 = XYZ_2[1]
            w = XYZ_2[2]-z_0

            #inatilise the overal variables

            warping_magnitude = 0.0
            stress_magnitude =0.0
            A = 0.0
            wc = np.zeros((np.shape(element_array)[0],2), dtype=np.float64)
            rc = np.zeros((np.shape(element_array)[0],2), dtype=np.float64)
            sc = np.zeros((np.shape(element_array)[0],2), dtype=np.float64)

            for i in range(np.shape(element_array)[0]):

                ###############################################################################################
                #warping
                ###############################################################################################
                (X0_0,Y0_0,X1_0,Y1_0, X2_0,Y2_0, X3_0,Y3_0) = element_array[i]
                AFxy = 1
                AFz  = 1



                condition = (df1['x'] == X0_0) & (df1['y'] == Y0_0)
                b = df1.index[condition].tolist()
                X0_2 = x_2[b[0]]
                Y0_2 = y_2[b[0]]
                X0_1 = x_1[b[0]]
                Y0_1 = y_1[b[0]]

                W0 = w[b[0]]


                condition = (df1['x'] == X1_0) & (df1['y'] == Y1_0)
                b = df1.index[condition].tolist()
                X1_2 = x_2[b[0]]
                Y1_2 = y_2[b[0]]
                X1_1 = x_1[b[0]]
                Y1_1 = y_1[b[0]]

                W1 = w[b[0]]

                condition = (df1['x'] == X2_0) & (df1['y'] == Y2_0)
                b = df1.index[condition].tolist()
                X2_2 = x_2[b[0]]
                Y2_2 = y_2[b[0]]
                X2_1 = x_1[b[0]]
                Y2_1 = y_1[b[0]]


                W2 = w[b[0]]


                condition = (df1['x'] == X3_0) & (df1['y'] == Y3_0)
                b = df1.index[condition].tolist()
                X3_2 = x_2[b[0]]
                Y3_2 = y_2[b[0]]
                X3_1 = x_1[b[0]]
                Y3_1 = y_1[b[0]]



                W3 = w[b[0]]


                # get the location of the warping shear centre for the element

                v1 = np.array([X2_2-X0_2, Y2_2-Y0_2])
                v2 = np.array([X3_2-X1_2, Y3_2-Y1_2])
                dw_1 = W2-W0
                dw_2 = W3-W1
                dS_1 = np.linalg.norm(v1)
                dS_2 = np.linalg.norm(v2)

                v1_perpendicular = dw_1/dS_1**2*np.matmul(np.array([[0,-1],[1,0]]),v1)
                v2_perpendicular = dw_2/dS_2**2*np.matmul(np.array([[0,-1],[1,0]]),v2)

                [xc,yc] = np.array([X2_2,Y2_2]) + np.transpose(v1_perpendicular)
                [xa,ya] = np.array([X0_2,Y0_2]) + np.transpose(v1_perpendicular)
                [xd,yd] = np.array([X3_2,Y3_2]) + np.transpose(v2_perpendicular)
                [xb,yb] = np.array([X1_2,Y1_2]) + np.transpose(v2_perpendicular)

                a0 = ya - yc
                b0 = xc - xa
                c0 = (ya - yc)*xc + (xc - xa)*yc

                a1 = yb - yd
                b1 = xd - xb
                c1 = (yb - yd)*xc + (xd - xb)*yc

                c_vector=np.array([c0,c1])

                ab = np.array([[a0,b0],[a1,b1]])
                x_wc, y_wc = np.matmul(np.linalg.inv(ab),c_vector)
                wc[i] = [x_wc, x_wc]

                w_mean = (W0+W1+W2+W3)/4
                ###############################################################################################
                #Rotation
                ###############################################################################################

                m_array = np.zeros(4)
                c_array = np.zeros(4)

                X1 = [X0_1, X1_1, X2_1, X3_1]
                X0 = [X0_0, X1_0, X2_0, X3_0]

                Y1 = [Y0_1, Y1_1, Y2_1, Y3_1]
                Y0 = [Y0_0, Y1_0, Y2_0, Y3_0]

                for i in range(4):
                    v1 = np.array([X1[i]-X0[i], Y1[i]-Y0[i]])
                    v1_unit = v1/np.linalg.norm(v1)
                    v1_perpendicular = np.matmul(np.array([[0,-1],[1,0]]),v1)
                    m= v1_perpendicular[1]/v1_perpendicular[0]
                    c = -m*X0[i]+Y0[i]
                    m_array[i] = m
                    c_array[i] = c

                A = np.vstack([-m_array, np.ones(len(m_array))]).T
                x_rc, y_rc = (np.linalg.lstsq(A, c_array, rcond=None)[0])
                rc[i] = [x_rc, y_rc]
                ###############################################################################################
                #stress
                ###############################################################################################

                df2 = self.S_df.loc[self.S_df["z"]==z]

                condition = (df2['x'] == X0_0) & (df2['y'] == Y0_0)
                b = df2.index[condition].tolist()
                S0 = self.S_df["S33"][b[0]]

                condition = (df2['x'] == X1_0) & (df2['y'] == Y1_0)
                b = df2.index[condition].tolist()
                S1 = self.S_df["S33"][b[0]]

                condition = (df2['x'] == X2_0) & (df2['y'] == Y2_0)
                b = df2.index[condition].tolist()
                S2 = self.S_df["S33"][b[0]]

                condition = (df2['x'] == X3_0) & (df2['y'] == Y3_0)
                b = df2.index[condition].tolist()
                S3 = self.S_df["S33"][b[0]]

                s_mean = (S0+S1+S2+S3)/4


                ds_1 = S2-S0
                ds_2 = S3-S1


                v1_perpendicular = ds_1/dS_1**2*np.matmul(np.array([[0,-1],[1,0]]),v1)
                v2_perpendicular = ds_2/dS_2**2*np.matmul(np.array([[0,-1],[1,0]]),v2)

                [xc,yc] = np.array([X2_2,Y2_2]) + np.transpose(v1_perpendicular)
                [xa,ya] = np.array([X0_2,Y0_2]) + np.transpose(v1_perpendicular)
                [xd,yd] = np.array([X3_2,Y3_2]) + np.transpose(v2_perpendicular)
                [xb,yb] = np.array([X1_2,Y1_2]) + np.transpose(v2_perpendicular)

                a0 = ya - yc
                b0 = xc - xa
                c0 = (ya - yc)*xc + (xc - xa)*yc

                a1 = yb - yd
                b1 = xd - xb
                c1 = (yb - yd)*xc + (xd - xb)*yc

                c_vector=np.array([c0,c1])

                ab = np.array([[a0,b0],[a1,b1]])
                x_sc, y_sc = np.matmul(np.linalg.inv(ab),c_vector)
                sc[i] = [x_sc, y_sc]

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

            StressMagnitude = stress_magnitude/A
            WarpingMagnitude = warping_magnitude/A

            MeanWC = np.mean(wc, axis=0)
            MeanRC = np.mean(rc, axis=0)
            MeanSC = np.mean(sc, axis=0)

            SpreadWC = np.std(wc, axis=0)
            SpreadRC = np.std(rc, axis=0)
            SpreadSC = np.std(sc, axis=0)

            data = {
                "GlobalDisplacementVector": GlobalDisplacementVector,
                "GlobalRotationVector": GlobalRotationVector,
                "WarpingMagnitude": WarpingMagnitude,
                "StressMagnitude": StressMagnitude,
                "MeanRC": MeanRC,
                "SpreadRC": SpreadRC,
                "MeanWC": MeanWC,
                "SpreadWC": SpreadWC,
                "MeanSC": MeanSC,
                "SpreadSC": SpreadSC,
            }

            dfr = pd.DataFrame(data = data, index = [z])
            dfr.index.name = "z"
            main_df = main_df.append(dfr, ignore_index = False)
            main_df.to_csv(main_information_csv)

        return main_df, extra_df
