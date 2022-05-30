import pandas as pd
import numpy as np



df = pd.read_csv("naca0024.csv", header = 0, usecols = [0,1])
df.columns=["x", "y" ]
df = df.astype(np.float64)

x= df["x"].values
y= df["y"].values
print(df)






#!/usr/bin/env python
import numpy as np
import matplotlib.patches
import matplotlib.pyplot as plt


class CurvedPatch(matplotlib.patches.Polygon):
    def __init__(self, path, width, *args, **kwargs):
        vertices = self.get_vertices(path, width)
        matplotlib.patches.Polygon.__init__(self, list(map(tuple, vertices)),
                                            closed=True,
                                            *args, **kwargs)

    def get_vertices(self, path, width):
        print(path)
        left = self._get_parallel_path(path, -width/2)
        right = self._get_parallel_path(path, width/2)
        full = np.concatenate([left, right[::-1]])
        return full


    def _get_parallel_path(path, delta):
        # initialise output
        offset = np.zeros_like(path)

        # use the previous and the following point to
        # determine the tangent at each point in the path;
        for ii in range(1, len(path)-1):
            offset[ii] += _get_shift(path[ii-1], path[ii+1], delta)

        # handle start and end points
        offset[0] = _get_shift(path[0], path[1], delta)
        offset[-1] = _get_shift(path[-2], path[-1], delta)

        return path + offset


    def _get_shift(p1, p2, delta):
        # unpack coordinates
        x1, y1 = p1
        x2, y2 = p2

        # get orthogonal unit vector;
        # adapted from https://stackoverflow.com/a/16890776/2912349
        v = np.r_[x2-x1, y2-y1]   # vector between points
        v = v / np.linalg.norm(v) # unit vector

        w = np.r_[-v[1], v[0]]    # orthogonal vector
        w = w / np.linalg.norm(w) # orthogonal unit vector

        # check that vectors are indeed orthogonal
        assert np.isclose(np.dot(v, w), 0.)

        # rescale unit vector
        dx, dy = delta * w

        return dx, dy


    def simple_test():

        x = np.linspace(-1, 1, 1000)
        y = np.sqrt(1. - x**2)
        path = np.c_[x, y]

        curve = CurvedPatch(path, 0.1, facecolor='red', alpha=0.5)

        fig, ax = plt.subplots(1,1)
        ax.add_artist(curve)
        ax.plot(x, y) # plot path for reference
        plt.show()


    def complicated_test():

        random_points = np.random.rand(10, 2)

        # Adapted from https://stackoverflow.com/a/35007804/2912349
        import scipy.interpolate as si

        def scipy_bspline(cv, n=100, degree=3, periodic=False):
            """ Calculate n samples on a bspline

                cv :      Array ov control vertices
                n  :      Number of samples to return
                degree:   Curve degree
                periodic: True - Curve is closed
            """
            cv = np.asarray(cv)
            count = cv.shape[0]

            # Closed curve
            if periodic:
                kv = np.arange(-degree,count+degree+1)
                factor, fraction = divmod(count+degree+1, count)
                cv = np.roll(np.concatenate((cv,) * factor + (cv[:fraction],)),-1,axis=0)
                degree = np.clip(degree,1,degree)

            # Opened curve
            else:
                degree = np.clip(degree,1,count-1)
                kv = np.clip(np.arange(count+degree+1)-degree,0,count-degree)

            # Return samples
            max_param = count - (degree * (1-periodic))
            spl = si.BSpline(kv, cv, degree)
            return spl(np.linspace(0,max_param,n))

        x, y = scipy_bspline(random_points, n=1000).T
        path = np.c_[x, y]

        curve = CurvedPatch(path, 0.1, facecolor='red', alpha=0.5)

        fig, ax = plt.subplots(1,1)
        ax.add_artist(curve)
        ax.plot(x, y) # plot path for reference
        plt.show()


path = zip(x,y)

CurvedPatch(path, 0.2)







# if __name__ == '__main__':
#     plt.ion()
#     simple_test()
#     complicated_test()
