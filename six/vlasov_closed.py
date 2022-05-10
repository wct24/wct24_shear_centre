import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#not joined




#define the sectors:
d = {"x_0":[0, 0.4, 0.4, 0],
     "y_0":[0.4,  0.4, -0.4, -0.4 ],
     "x_1":[ 0.4, 0.4,0, 0],
     "y_1":[  0.4,-0.4,-0.4, 0.4],
}

df_xy = pd.DataFrame(data=d, dtype=np.float64)

# find the neutral axes:

def turn_into_principal(df):
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

    return df_uv,NA_x ,NA_y

df_uv,NA_x ,NA_y = turn_into_principal(df_xy)



def I_uu(df):
    I_uu =0.0
    for i in df.index:
        length = np.sqrt((df["u_1"][i]-df["u_0"][i])**2 + (df["v_1"][i]-df["v_0"][i])**2)
        sin_theta_u =abs(  (df["v_1"][i]-df["v_0"][i])/length )
        I_11 = (length**3)/12
        I_uu += ((df["v_1"][i]+df["v_0"][i])/2)**2*length + I_11*sin_theta_u
    return I_uu

def I_vv(df):
    I_vv =0.0
    for i in df.index:
        length = np.sqrt((df["u_1"][i]-df["u_0"][i])**2 + (df["v_1"][i]-df["v_0"][i])**2)
        sin_theta_v =abs(  (df["u_1"][i]-df["u_0"][i])/length )
        I_11 = (length**3)/12
        I_vv += ((df["u_1"][i]+df["u_0"][i])/2)**2*length + I_11*sin_theta_v
    return I_vv

I_uu = I_uu(df_uv)
I_vv = I_vv(df_uv)
print(I_vv)
print("----------")


def coefficient(x,y):
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



def I_uw_vw(df, pole, display_w=False):
    # first define the w initialy the w at the start of the first sector will be zero
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



    if df["u_0"][0] == df["u_1"].iloc[-1] and df["v_0"][0] == df["v_1"].iloc[-1]:
        print("hello")

        w_matrix = np.zeros([len(df.index),len(df.index)*2])
        for n in df.index:
            w_list = [0]
            w =0.0
            wl_total= 0.0
            s_total =0.0

            for i in df.index:
                #make the indeces circular
                k = i+n

                while k >len(df.index)-1:
                    k = i+n - len(df.index)
                length = np.sqrt((df["u_1"][k]-df["u_0"][k])**2 + (df["v_1"][k]-df["v_0"][k])**2)
                s_total += length
                segment_vector = np.array([df["u_1"][k]-df["u_0"][k],df["v_1"][k]-df["v_0"][k],0.0])
                r_vector =   np.array([(df["u_1"][k]+df["u_0"][k])/2-pole[0],(df["v_1"][k]+df["v_0"][k])/2-pole[1],0.0])
                change_in_warping = np.cross(r_vector, segment_vector)[2]
                w += change_in_warping
                #area of a trapezium:
                wl_total += length*(w-change_in_warping/2)
                w_list.append(w)
            # impose the Sw = o condition, find the average value of w:
            w_mean = wl_total/s_total
            w_array = np.array(w_list)-w_mean
            print("w_array = ", w_array)
                # # find Iuu:
                # I_uw = 0.0
                # I_vw = 0.0

            # w_mean = wl_total/s_total
            # w_array = np.array(w_list)-w_mean

            # when n = 0
            # w_matrix[n][0] = w_array[-1]
            # w_matrix[n][1] = w_array[0]
            # w_matrix[n][2] = w_array[1]
            # w_matrix[n][3] = w_array[1]
            # # and so on...
            # when n = 1
            # w_matrix[n][2] = w_array[-1]
            # w_matrix[n][3] = w_array[0]
            # w_matrix[n][4] = w_array[1]
            # w_matrix[n][5] = w_array[1]
            # w_matrix[n][6] = w_array[2]
            # w_matrix[n][7] = w_array[2]
            # w_matrix[n][0] = w_array[3]
            # w_matrix[n][1] = w_array[3]

            # j = 2*n
            # if j >len(df.index)*2-1:
            #     j = j - len(df.index)


            def j(x, n):
                j = 2*n + x
                while j >len(df.index)*2-1:
                    j = j - 2*len(df.index)
                return j


            w_matrix[n][j(0,n)] = w_array[-1]/4
            w_matrix[n][j(1,n)] = w_array[0]/4
            w_matrix[n][j(2,n)] = w_array[1]/4
            w_matrix[n][j(3,n)] = w_array[1]/4
            w_matrix[n][j(4,n)] = w_array[2]/4
            w_matrix[n][j(5,n)] = w_array[2]/4
            print(j(6,n))
            w_matrix[n][j(6,n)] = w_array[3]/4
            w_matrix[n][j(7,n)] = w_array[3]/4

            for i in range(len(2*df.index)):
                if i == 0:
                    w_matrix[n][j(i,n)] = w_array[-1]/4
                elif i == 1:
                    w_matrix[n][j(i,n)] = w_array[0]/4
                else:
                    w_matrix[n][j(2,n)] = w_array[i//2]/4


        w_trial = np.sum(w_matrix,axis=0)




        # find Iuu:
    I_uw = 0.0
    I_vw = 0.0
    #If closed wall need to adjust:


    for i in df.index:
        # com of trapezium:
        length = np.sqrt((df["u_1"][i]-df["u_0"][i])**2 + (df["v_1"][i]-df["v_0"][i])**2)

        # The integrand is always quadratic therefore you can use 3 points in w x/y space to get the quadraticdegbh
        #for Iuw:

        def j2(x, n):
                j = 2*n + x
                while j >len(df.index)*2-1:
                    j = j - 2*len(df.index)
                return j

        w_trial[1]
        print(i, j2(1,i), j2(2,i))


        wv_0 = w_trial[j2(1,i)]*df["v_0"][i]
        print(wv_0)
        wv_mid = (w_trial[j2(1,i)]+w_trial[j2(2,i)])*(df["v_0"][i]+df["v_1"][i])/4
        print(wv_mid)
        wv_1 = w_trial[j2(2,i)]*df["v_1"][i]

        a,b,c = coefficient([0,0.5, 1 ],[wv_0,wv_mid, wv_1 ])
        # given the a,b,c it is easy to get the definite integral

        integral_v = length*(6*c+3*b+2*a)/6
        I_uw += integral_v

        wu_0 = w_trial[j2(1,i)]*df["u_0"][i]
        wu_mid = (w_trial[j2(1,i)]+w_trial[j2(2,i)])*(df["u_0"][i]+df["u_1"][i])/4
        wu_1 = w_trial[j2(2,i)]*df["u_1"][i]

        a,b,c = coefficient([0,0.5, 1 ],[wu_0,wu_mid, wu_1 ])
        # given the a,b,c it is easy to get the definite integral
        integral_u = length*(6*c+3*b+2*a)/6

        I_vw += integral_u
    return I_uw, I_vw



A = [-5.0,5.0]


I_uw, I_vw =I_uw_vw(df_uv, A, display_w=False)



print("---------- shear centre ----------------- ")
print("centroid = " , [NA_x, NA_y])
print(I_uw/I_uu)
print(I_vw/I_vv)

print("principal sectorial point = " , [I_uw/I_uu + NA_x + A[0], -I_vw/I_vv+ NA_y + A[1]])



