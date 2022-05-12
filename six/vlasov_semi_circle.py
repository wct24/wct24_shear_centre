import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def semi_circle(n=100):
    theta = np.linspace(-np.pi/2, np.pi/2, 100)
    # print(theta)
    x = np.cos(theta)
    y = np.sin(theta)
    # plt.plot(x,y)
    # plt.show()
    x_0 = x[:-1]
    y_0 = y[:-1]

    x_1 = x[1:]
    y_1 = y[1:]
    # print(len(x))
    # print(len(x_1))
    # print(len(x_0))
    return x_0, y_0, x_1, y_1



x_0, y_0, x_1, y_1 = semi_circle()


#define the sectors:
d = {"x_0":x_0,
     "y_0":y_0,
     "x_1":x_1,
     "y_1":y_1,
}

# df_xy = pd.DataFrame(data=d, dtype=np.float64)

# # find the neutral axes:

# def turn_into_principal(df):
#     A = 0.0
#     Ax = 0.0
#     Ay = 0.0
#     for i in df.index:
#         length = np.sqrt((df["x_1"][i]-df["x_0"][i])**2 + (df["y_1"][i]-df["y_0"][i])**2)
#         x =  (df["x_1"][i]+df["x_0"][i])/2
#         y =  (df["y_1"][i]+df["y_0"][i])/2
#         A += length
#         Ax += length*x
#         Ay += length*y
#     NA_x = Ax/A
#     NA_y = Ay/A

#     df_uv = df - [NA_x,NA_y,NA_x,NA_y]
#     # rename the columns:
#     df_uv.columns = ['u_0', 'v_0', 'u_1', 'v_1']

#     return df_uv,NA_x ,NA_y

# df_uv,NA_x ,NA_y = turn_into_principal(df_xy)



# def I_uu(df):
#     I_uu =0.0
#     for i in df.index:
#         length = np.sqrt((df["u_1"][i]-df["u_0"][i])**2 + (df["v_1"][i]-df["v_0"][i])**2)
#         sin_theta_u =abs(  (df["v_1"][i]-df["v_0"][i])/length )
#         I_11 = (length**3)/12
#         I_uu += ((df["v_1"][i]+df["v_0"][i])/2)**2*length + I_11*sin_theta_u
#     return I_uu

# def I_vv(df):
#     I_vv =0.0
#     for i in df.index:
#         length = np.sqrt((df["u_1"][i]-df["u_0"][i])**2 + (df["v_1"][i]-df["v_0"][i])**2)
#         sin_theta_v =abs(  (df["u_1"][i]-df["u_0"][i])/length )
#         I_11 = (length**3)/12
#         I_vv += ((df["u_1"][i]+df["u_0"][i])/2)**2*length + I_11*sin_theta_v
#     return I_vv

# I_uu = I_uu(df_uv)
# I_vv = I_vv(df_uv)
# print(I_vv)
# print("----------")


# def coefficient(x,y):
#     x_1 = x[0]
#     x_2 = x[1]
#     x_3 = x[2]
#     y_1 = y[0]
#     y_2 = y[1]
#     y_3 = y[2]

#     a = y_1/((x_1-x_2)*(x_1-x_3)) + y_2/((x_2-x_1)*(x_2-x_3)) + y_3/((x_3-x_1)*(x_3-x_2))

#     b = (-y_1*(x_2+x_3)/((x_1-x_2)*(x_1-x_3))
#          -y_2*(x_1+x_3)/((x_2-x_1)*(x_2-x_3))
#          -y_3*(x_1+x_2)/((x_3-x_1)*(x_3-x_2)))

#     c = (y_1*x_2*x_3/((x_1-x_2)*(x_1-x_3))
#         +y_2*x_1*x_3/((x_2-x_1)*(x_2-x_3))
#         +y_3*x_1*x_2/((x_3-x_1)*(x_3-x_2)))

#     return a,b,c



# def I_uw_vw(df, pole, display_w=False):
#     # first define the w initialy the w at the start of the first sector will be zero
#     w_list = [0]
#     w =0.0
#     wl_total= 0.0
#     s_total =0.0
#     for i in df.index:
#         length = np.sqrt((df["u_1"][i]-df["u_0"][i])**2 + (df["v_1"][i]-df["v_0"][i])**2)
#         s_total += length
#         segment_vector = np.array([df["u_1"][i]-df["u_0"][i],df["v_1"][i]-df["v_0"][i],0.0])
#         r_vector =   np.array([(df["u_1"][i]+df["u_0"][i])/2-pole[0],(df["v_1"][i]+df["v_0"][i])/2-pole[0],0.0])
#         change_in_warping = np.cross(r_vector, segment_vector)[2]
#         w += change_in_warping
#         #area of a trapezium:
#         wl_total += length*(w-change_in_warping/2)
#         w_list.append(w)
#     # impose the Sw = o condition, find the average value of w:
#     w_mean = wl_total/s_total
#     w_array = np.array(w_list)-w_mean
#     print(w_array)
#     # find Iuu:
#     I_uw = 0.0
#     I_vw = 0.0
#     for i in df.index:
#         # com of trapezium:
#         length = np.sqrt((df["u_1"][i]-df["u_0"][i])**2 + (df["v_1"][i]-df["v_0"][i])**2)

#         # The integrand is always quadratic therefore you can use 3 points in w x/y space to get the quadraticdegbh
#         #for Iuw:
#         wv_0 = w_array[i]*df["v_0"][i]
#         print(wv_0)
#         wv_mid = (w_array[i]+w_array[i+1])*(df["v_0"][i]+df["v_1"][i])/4
#         print(wv_mid)
#         wv_1 = w_array[i+1]*df["v_1"][i]

#         a,b,c = coefficient([0,0.5, 1 ],[wv_0,wv_mid, wv_1 ])
#         # given the a,b,c it is easy to get the definite integral


#         integral = length*(6*c+3*b+2*a)/6


#         I_uw += integral
#         I_vw += 0
#     return I_uw, I_vw



# I_uw, I_vw =I_uw_vw(df_uv, [0.0,0.0], display_w=False)
# print(I_uu)
# print(I_uw)





# print("shear centre")
# print(NA_x)
# print(I_uw/I_uu)



class vlasov:
    def __init__(self, PointDictionary):
        self.df_xy = pd.DataFrame(data=PointDictionary, dtype=np.float64)
        self.df_uv, self.centroid = self.turn_into_principal(self.df_xy)

        self.u, self.v = self._coordinates()
        self.I_uu = self._I_uu(self.df_uv)
        self.I_vv = self._I_vv(self.df_uv)
        self.I_uw, self.I_vw =  self._I_uw_vw(self.df_uv)
        self.shear_centre = self._shear_centre()
        self.shear_centre_uv =self._shear_centre_uv()

    def _coefficient(self, x,y):
        x_1 = x[0]
        x_2 = x[1]
        x_3 = x[2]
        y_1 = y[0]
        y_2 = y[1]
        y_3 = y[2]

        a = y_1/((x_1-x_2)*(x_1-x_3)) + y_2/((x_2-x_1)*(x_2-x_3)) + y_3/((x_3-x_1)*(x_3-x_2))

        b = (-y_1*(x_2+x_3)/((x_1-x_2)*(x_1-x_3))
             -y_2*(x_1+x_3)/((x_2-x_1)*(x_2-x_3))
             -y_3*(x_1+x_2)/((x_3-x_1)*(x_3-x_2)))

        c = (y_1*x_2*x_3/((x_1-x_2)*(x_1-x_3))
            +y_2*x_1*x_3/((x_2-x_1)*(x_2-x_3))
            +y_3*x_1*x_2/((x_3-x_1)*(x_3-x_2)))

        return a,b,c

    def _coordinates(self):
        u_0 = self.df_uv["u_0"].values
        u_1 = self.df_uv["u_1"].values
        u = np.append(u_0, u_1[-1])

        v_0 = self.df_uv["v_0"].values
        v_1 = self.df_uv["v_1"].values
        v = np.append(v_0, v_1[-1])
        return u, v




    def turn_into_principal(self, df):
        A = 0.0
        Ax = 0.0
        Ay = 0.0
        for i in df.index:
            length = np.sqrt((df["x_1"][i]-df["x_0"][i])**2 + (df["y_1"][i]-df["y_0"][i])**2)
            x =  (df["x_1"][i]+df["x_0"][i])/2
            y =  (df["y_1"][i]+df["y_0"][i])/2
            A += length
            Ax += length*x
            Ay += length*y
        NA_x = Ax/A
        NA_y = Ay/A

        df_uv = df - [NA_x,NA_y,NA_x,NA_y]
        # rename the columns:
        df_uv.columns = ['u_0', 'v_0', 'u_1', 'v_1']

        return df_uv,[NA_x ,NA_y]

    def _I_uu(self, df):
        I_uu =0.0
        for i in df.index:
            length = np.sqrt((df["u_1"][i]-df["u_0"][i])**2 + (df["v_1"][i]-df["v_0"][i])**2)
            sin_theta_u =abs(  (df["v_1"][i]-df["v_0"][i])/length )
            I_11 = (length**3)/12
            I_uu += ((df["v_1"][i]+df["v_0"][i])/2)**2*length + I_11*sin_theta_u
        return I_uu

    def _I_vv(self, df):
        I_vv =0.0
        for i in df.index:
            length = np.sqrt((df["u_1"][i]-df["u_0"][i])**2 + (df["v_1"][i]-df["v_0"][i])**2)
            sin_theta_v =abs(  (df["u_1"][i]-df["u_0"][i])/length )
            I_11 = (length**3)/12
            I_vv += ((df["u_1"][i]+df["u_0"][i])/2)**2*length + I_11*sin_theta_v
        return I_vv
    def _I_uw_vw(self,  pole=[0,0], display_w=False):
        # first define the w initialy the w at the start of the first sector will be zero
        pole=[0.0, 0.0]
        df=self.df_uv
        w_list = [0]
        w =0.0
        wl_total= 0.0
        s_total =0.0
        for i in df.index:
            length = np.sqrt((df["u_1"][i]-df["u_0"][i])**2 + (df["v_1"][i]-df["v_0"][i])**2)
            s_total += length
            segment_vector = np.array([df["u_1"][i]-df["u_0"][i],df["v_1"][i]-df["v_0"][i],0.0])
            r_vector =   np.array([(df["u_1"][i]+df["u_0"][i])/2-pole[0],(df["v_1"][i]+df["v_0"][i])/2-pole[0],0.0])
            change_in_warping = np.cross(r_vector, segment_vector)[2]
            w += change_in_warping
            #area of a trapezium:
            wl_total += length*(w-change_in_warping/2)
            w_list.append(w)
        # impose the Sw = o condition, find the average value of w:
        w_mean = wl_total/s_total
        w_array = np.array(w_list)-w_mean

        # find Iuu:
        I_uw = 0.0
        I_vw = 0.0
        for i in df.index:
            # com of trapezium:
            length = np.sqrt((df["u_1"][i]-df["u_0"][i])**2 + (df["v_1"][i]-df["v_0"][i])**2)

            # The integrand is always quadratic therefore you can use 3 points in w x/y space to get the quadraticdegbh
            #for Iuw:
            wv_0 = w_array[i]*df["v_0"][i]
            wv_mid = (w_array[i]+w_array[i+1])*(df["v_0"][i]+df["v_1"][i])/4

            wv_1 = w_array[i+1]*df["v_1"][i]

            a,b,c = self._coefficient([0,0.5, 1 ],[wv_0,wv_mid, wv_1 ])
            # given the a,b,c it is easy to get the definite integral


            integral = length*(6*c+3*b+2*a)/6

            I_uw += integral
            I_vw += 0
        return I_uw, I_vw

    def _shear_centre(self):



        return [self.I_uw/self.I_uu + self.centroid[0], -self.I_vw / self.I_vv + self.centroid[1]]
    def _shear_centre_uv(self):

        return [self.I_uw/self.I_uu, -self.I_vw / self.I_vv ]





    def plot_w(self):
        pole=[2/np.pi,0]
        df = self.df_uv
        w_list = [0]
        w =0.0
        wl_total= 0.0
        s_total =0.0
        for i in df.index:
            length = np.sqrt((df["u_1"][i]-df["u_0"][i])**2 + (df["v_1"][i]-df["v_0"][i])**2)
            s_total += length
            segment_vector = np.array([df["u_1"][i]-df["u_0"][i],df["v_1"][i]-df["v_0"][i],0.0])
            r_vector =   np.array([(df["u_1"][i]+df["u_0"][i])/2-pole[0],(df["v_1"][i]+df["v_0"][i])/2-pole[1],0.0])
            change_in_warping = np.cross(r_vector, segment_vector)[2]
            w += change_in_warping
            #area of a trapezium:
            wl_total += length*(w-change_in_warping/2)
            w_list.append(w)
        # impose the Sw = o condition, find the average value of w:
        w_mean = wl_total/s_total
        w_array = np.array(w_list)-w_mean
        print(w_array)
        u_array = self.u
        v_array = self.v

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.plot(u_array, v_array, w_array )
        plt.show()
         # find Iuu:
        I_uw = 0.0
        I_vw = 0.0
        for i in df.index:
            # com of trapezium:
            length = np.sqrt((df["u_1"][i]-df["u_0"][i])**2 + (df["v_1"][i]-df["v_0"][i])**2)

            # The integrand is always quadratic therefore you can use 3 points in w x/y space to get the quadraticdegbh
            #for Iuw:
            wv_0 = w_array[i]*df["v_0"][i]
            wv_mid = (w_array[i]+w_array[i+1])*(df["v_0"][i]+df["v_1"][i])/4

            wv_1 = w_array[i+1]*df["v_1"][i]

            a,b,c = self._coefficient([0,0.5, 1 ],[wv_0,wv_mid, wv_1 ])
            # given the a,b,c it is easy to get the definite integral


            integral = length*(6*c+3*b+2*a)/6

            I_uw += integral
            I_vw += 0
        print("I_uw : ", I_uw, "I_vw : ", I_vw, )



# d = {"x_0":[0, 0.4, 0.4],
#      "y_0":[0.4, 0.4, -0.4 ],
#      "x_1":[0.4,0.4,0],
#      "y_1":[0.4,-0.4,-0.4]
# }

print(vlasov(d).shear_centre_uv)

print(vlasov(d).plot_w())

