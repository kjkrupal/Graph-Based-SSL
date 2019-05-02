import scipy.io as sio
from scipy import sparse
from sklearn.metrics.pairwise import euclidean_distances

def generateMat():
    
    for i in range(8):

        print("Generating data for user " + str(i+1))

        # Data for ith user
        begin = i * 1140
        end = (i+1) * 1140
        X = x.iloc[begin:end].values

        # Compute sparse matrix
        A = rbf_kernel(X)
        A [A == 1 ] = 0
        A = sparse.csr_matrix(A)

        # Compute pairwise distance
        ecd = euclidean_distances(X)

        # Number of nearest neighbors
        knn_param = 10
        
        # Calculating distance of KNN
        knn_distance = np.zeros((1140,))
        for j in range(1140):
            temp = np.sort(ecd[j])
            knn_distance[j] = temp[knn_param + 1]
        
        # Compute sigma
        sigma = 1/3 * np.mean(knn_distance)
        
        # Membership function
        mem_fn = y[begin:end]
        
        fname = 'set' + str(i+1) + '.mat'
        
        sio.savemat(fname, {'A': A, 'X': X, 'mem_fn' : mem_fn, 'sigma' : sigma})

generateMat()