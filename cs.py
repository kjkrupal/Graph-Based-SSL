import scipy.io as sio
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

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

        # Compute similarity
        cs = cosine_similarity(X)

        # Number of nearest neighbors
        threshold = 0.7
        
        # Calculating distance of KNN
        cos_sim = np.zeros((1140,))
        for j in range(1140):
            knn_distance[j] = temp[temp > threshold]
        
        # Compute sigma
        sigma = 1/3 * np.mean(cos_sim)
        
        # Membership function
        mem_fn = y[begin:end]
        
        fname = 'set' + str(i+1) + '.mat'
        
        sio.savemat(fname, {'A': A, 'X': X, 'mem_fn' : mem_fn, 'sigma' : sigma})

generateMat()