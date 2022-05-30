import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd





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


    def plot_w_P(self):
        # pole=self.shear_centre_uv
        pole=self.shear_centre_uv
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

        # def perpendicular( a ) :
        #     b = np.empty_like(a)
        #     b[0] = -a[1]
        #     b[1] = a[0]
        #     return b

        # def normalise(a):
        #     a = np.array(a)
        #     return a/np.linalg.norm(a)



        ax.plot(u_array, v_array, c='grey')
        # perpendicular_vector_array = np.zeros([len(u_array),2])
        # print(perpendicular_vector_array)
        # for i in range(len(u_array)) :
        #     if i == 0:
        #         du = u_array[1]-u_array[0]
        #         dv = u_array[1] - u_array[0]
        #     if i == len(perpendicular_vector_array)-1:
        #         du = u_array[-1]-u_array[-2]
        #         dv = u_array[-1] - u_array[-2]
        #     else:
        #         du = u_array[i+1]-u_array[i-1]
        #         dv = u_array[i+1] - u_array[i-1]

        #     # print("p", perpendicular(normalise([du,dv])))

        #     perpendicular_vector_array[i] = w_array[i]*perpendicular(normalise([du,dv]))

        # print(perpendicular_vector_array)




        x  = u_array
        y = v_array
        z = w_array

        def get_colour(mean_omega):
            # mean_omega = np.mean(w_array)
            range_w =  w_array.max()-w_array.min()
            Float_between_0_and_1 = (mean_omega-w_array.min())/range_w
            return Float_between_0_and_1

        x_offset = u_array.min()- 0.2*(u_array.max()-u_array.min())
        y_offset = v_array.min()- 0.2*(v_array.max()-v_array.min())
        z_offset = w_array.min()- 0.2*(w_array.max()-w_array.min())




        for i in range(1,len(x)):
            ax.plot(x[i-1:i+1], y[i-1:i+1], z[i-1:i+1], c = plt.cm.plasma(get_colour(z[i])), linewidth = 2)
            ax.plot(x[i-1:i+1], y[i-1:i+1], [z_offset,z_offset ], c = plt.cm.seismic(get_colour(z[i])))
            ax.plot(x[i-1:i+1], [-y_offset,-y_offset], z[i-1:i+1], c = plt.cm.seismic(get_colour(z[i])))
            ax.plot([x_offset, x_offset], y[i-1:i+1], z[i-1:i+1], c = plt.cm.seismic(get_colour(z[i])))
        ax.set_zlim(bottom= z_offset*0.97, top = -z_offset*0.97)
        ax.set_xlim(left=x_offset *0.97)
        ax.set_ylim(top=-y_offset*0.97)




        ax.set_box_aspect([1,(v_array.max()-v_array.min())/(u_array.max()-u_array.min()),1])

        ax.set_xlabel("$x / m$")
        ax.set_ylabel("$y / m$")
        ax.set_zlabel("$\omega_P / m^2$")

        ax.locator_params(axis='z', nbins=3)
        ax.locator_params(axis='x', nbins=2)
        ax.locator_params(axis='y', nbins=2)
        fig.set_figwidth(6.25)
        fig.set_dpi(1000)




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

    def plot_w_A(self):
        # pole=self.shear_centre_uv
        pole=[0,0]
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

        # def perpendicular( a ) :
        #     b = np.empty_like(a)
        #     b[0] = -a[1]
        #     b[1] = a[0]
        #     return b

        # def normalise(a):
        #     a = np.array(a)
        #     return a/np.linalg.norm(a)



        ax.plot(u_array, v_array, c='grey')
        # perpendicular_vector_array = np.zeros([len(u_array),2])
        # print(perpendicular_vector_array)
        # for i in range(len(u_array)) :
        #     if i == 0:
        #         du = u_array[1]-u_array[0]
        #         dv = u_array[1] - u_array[0]
        #     if i == len(perpendicular_vector_array)-1:
        #         du = u_array[-1]-u_array[-2]
        #         dv = u_array[-1] - u_array[-2]
        #     else:
        #         du = u_array[i+1]-u_array[i-1]
        #         dv = u_array[i+1] - u_array[i-1]

        #     # print("p", perpendicular(normalise([du,dv])))

        #     perpendicular_vector_array[i] = w_array[i]*perpendicular(normalise([du,dv]))

        # print(perpendicular_vector_array)




        x  = u_array
        y = v_array
        z = w_array

        def get_colour(mean_omega):
            # mean_omega = np.mean(w_array)
            range_w =  w_array.max()-w_array.min()
            Float_between_0_and_1 = (mean_omega-w_array.min())/range_w
            return Float_between_0_and_1

        x_offset = u_array.min()- 0.2*(u_array.max()-u_array.min())
        y_offset = v_array.min()- 0.2*(v_array.max()-v_array.min())
        z_offset = w_array.min()- 0.2*(w_array.max()-w_array.min())




        for i in range(1,len(x)):
            ax.plot(x[i-1:i+1], y[i-1:i+1], z[i-1:i+1], c = plt.cm.plasma(get_colour(z[i])), linewidth = 2)
            ax.plot(x[i-1:i+1], y[i-1:i+1], [z_offset,z_offset ], c = plt.cm.seismic(get_colour(z[i])))
            ax.plot(x[i-1:i+1], [-y_offset,-y_offset], z[i-1:i+1], c = plt.cm.seismic(get_colour(z[i])))
            ax.plot([x_offset, x_offset], y[i-1:i+1], z[i-1:i+1], c = plt.cm.seismic(get_colour(z[i])))

        # ax.scatter(0,0,0, marker='X', c= "green")

        ax.set_zlim(bottom= z_offset*0.97, top = -z_offset*0.97)
        ax.set_xlim(left=x_offset *0.97)
        ax.set_ylim(top=-y_offset*0.97)




        ax.set_box_aspect([1,(v_array.max()-v_array.min())/(u_array.max()-u_array.min()),1])

        ax.set_xlabel("$x / m$")
        ax.set_ylabel("$y / m$")
        ax.set_zlabel("$ \omega_A / m^2$")

        ax.locator_params(axis='z', nbins=3)
        ax.locator_params(axis='x', nbins=2)
        ax.locator_params(axis='y', nbins=2)

        fig.set_figwidth(6.25)
        fig.set_dpi(1000)
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



def semi_circle(r, n=100):
    theta = np.linspace(-np.pi/2, np.pi/2, 100)
    # print(theta)
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    # plt.plot(x,y)
    # plt.show()
    x_0 = x
    y_0 = y

    x_1 = np.append(x[1:],x[0])
    y_1 = np.append(y[1:],y[0])
    # print(len(x))
    # print(len(x_1))
    # print(len(x_0))

    d = {
        "x_0":x_0,
        "y_0":y_0,
        "x_1":x_1,
        "y_1":y_1,
    }

    return d



fig = plt.figure()
ax = fig.add_subplot(projection='3d')

print(vlasov(semi_circle(0.40)).shear_centre_uv)
# plt.savefig("D:\\report\\figs\\introduction\\pcp1.png")
# plt.savefig("D:\\report\\figs\\introduction\\pcp1.pgf")



# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# vlasov(semi_circle(0.40)).plot_w_P()

# plt.savefig("D:\\report\\figs\\introduction\\pcp.png")
# plt.savefig("D:\\report\\figs\\introduction\\pcp.pgf")




# # vlasov(semi_circle(0.39)).plot_w()
# vlasov(semi_circle(0.40)).plot_w()
# vlasov(semi_circle(0.41)).plot_w()




# plt.show()

