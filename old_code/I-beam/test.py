


# Function to know if we have a CCW turn
def CCW(p1, p2, p3):
    if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
        return True
    return False

# Main function:
def GiftWrapping(S):
    n = len(S)
    P = [None] * n
    l = np.where(S[:,0] == np.min(S[:,0]))
    pointOnHull = S[l[0][0]]
    i = 0
    while True:
        P[i] = pointOnHull
        endpoint = S[0]
        for j in range(1,n):
            if (endpoint[0] == pointOnHull[0] and endpoint[1] == pointOnHull[1]) or not CCW(S[j],P[i],endpoint):
                endpoint = S[j]
        i = i + 1
        pointOnHull = endpoint
        if endpoint[0] == P[0][0] and endpoint[1] == P[0][1]:
            break
    for i in range(n):
        if P[-1] is None:
            del P[-1]
    return np.array(P)

def main():
    # try:
    #     N = int(sys.argv[1])
    # except:
    #     N = int(input("Introduce N: "))
    N=300
    # By default we build a random set of N points with coordinates in [0,300)x[0,300):
    P = np.array([(np.random.randint(0,300),np.random.randint(0,300)) for i in range(N)])
    print(P)
    df1 = u.loc[u["z"]==1.0]
    x_0 = df1["x"].values
    y_0 = df1["y"].values

    # P = np.array(sorted(list(zip(x_0,y_0)), key=lambda x: x[0]))

    print(P)

    L = GiftWrapping(P)

    # Plot the computed Convex Hull:
    plt.figure()
    plt.plot(L[:,0],L[:,1], 'b-', picker=5)
    plt.plot([L[-1,0],L[0,0]],[L[-1,1],L[0,1]], 'b-', picker=5)
    plt.plot(P[:,0],P[:,1],".r")
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
  main()




# Function to know if we have a CCW turn
def RightTurn(p1, p2, p3):
    if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
        return False
    return True

# Main algorithm:
def GrahamScan(P):
    P.sort()            # Sort the set of points
    L_upper = [P[0], P[1]]      # Initialize upper part
    # Compute the upper part of the hull
    for i in range(2,len(P)):
        L_upper.append(P[i])
        while len(L_upper) > 2 and not RightTurn(L_upper[-1],L_upper[-2],L_upper[-3]):
            del L_upper[-2]
    L_lower = [P[-1], P[-2]]    # Initialize the lower part
    # Compute the lower part of the hull
    for i in range(len(P)-3,-1,-1):
        L_lower.append(P[i])
        while len(L_lower) > 2 and not RightTurn(L_lower[-1],L_lower[-2],L_lower[-3]):
            del L_lower[-2]
    del L_lower[0]
    del L_lower[-1]
    L = L_upper + L_lower       # Build the full hull
    return np.array(L)

def main():
    # try:
    #     N = int(sys.argv[1])
    # except:
    #     N = int(input("Introduce N: "))

    # By default we build a random set of N points with coordinates in [0,300)x[0,300):
    # P = [(np.random.randint(0,300),np.random.randint(0,300)) for i in range(N)]
    df1 = u.loc[u["z"]==1.0]
    x_0 = df1["x"].values
    y_0 = df1["y"].values

    P = list(zip(x_0,y_0))

    print(P)


    L = GrahamScan(P)
    print(L)
    P = np.array(P)

    # Plot the computed Convex Hull:
    plt.figure()
    plt.plot(L[:,0],L[:,1], 'b-', picker=5)
    plt.plot([L[-1,0],L[0,0]],[L[-1,1],L[0,1]], 'b-', picker=5)
    plt.plot(P[:,0],P[:,1],".r")
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    main()





from scipy.spatial import Delaunay
import numpy as np


def alpha_shape(points, alpha, only_outer=True):
    """
    Compute the alpha shape (concave hull) of a set of points.
    :param points: np.array of shape (n,2) points.
    :param alpha: alpha value.
    :param only_outer: boolean value to specify if we keep only the outer border
    or also inner edges.
    :return: set of (i,j) pairs representing edges of the alpha-shape. (i,j) are
    the indices in the points array.
    """
    assert points.shape[0] > 3, "Need at least four points"

    def add_edge(edges, i, j):
        """
        Add an edge between the i-th and j-th points,
        if not in the list already
        """
        if (i, j) in edges or (j, i) in edges:
            # already added
            assert (j, i) in edges, "Can't go twice over same directed edge right?"
            if only_outer:
                # if both neighboring triangles are in shape, it's not a boundary edge
                edges.remove((j, i))
            return
        edges.add((i, j))

    tri = Delaunay(points)
    edges = set()
    # Loop over triangles:
    # ia, ib, ic = indices of corner points of the triangle
    for ia, ib, ic in tri.vertices:
        pa = points[ia]
        pb = points[ib]
        pc = points[ic]
        # Computing radius of triangle circumcircle
        # www.mathalino.com/reviewer/derivation-of-formulas/derivation-of-formula-for-radius-of-circumcircle
        a = np.sqrt((pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2)
        b = np.sqrt((pb[0] - pc[0]) ** 2 + (pb[1] - pc[1]) ** 2)
        c = np.sqrt((pc[0] - pa[0]) ** 2 + (pc[1] - pa[1]) ** 2)
        s = (a + b + c) / 2.0
        area = np.sqrt(s * (s - a) * (s - b) * (s - c))
        circum_r = a * b * c / (4.0 * area)
        if circum_r < alpha:
            add_edge(edges, ia, ib)
            add_edge(edges, ib, ic)
            add_edge(edges, ic, ia)
    return edges



def main():
    # try:
    #     N = int(sys.argv[1])
    # except:
    #     N = int(input("Introduce N: "))

    # By default we build a random set of N points with coordinates in [0,300)x[0,300):
    # P = [(np.random.randint(0,300),np.random.randint(0,300)) for i in range(N)]
    df1 = u.loc[u["z"]==1.0]
    x_0 = df1["x"].values
    y_0 = df1["y"].values

    P = np.array(list(zip(x_0,y_0)))

    print(P)


    L = alpha_shape(P,0.4, True)
    print(L)
    P = np.array(P)

    # Plot the computed Convex Hull:
    plt.figure()
    plt.scatter(L)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    main()









