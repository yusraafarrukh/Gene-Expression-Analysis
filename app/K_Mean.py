import numpy as np

def run_kmeans(X, k, max_iter=100):
    np.random.seed(42)

    # Step 1: Initialize centroids randomly
    random_indices = np.random.choice(X.shape[0], k, replace=False)
    centroids = X[random_indices]

    for i in range(max_iter):
        # Step 2: Compute distances between points and centroids
        distances = np.sqrt(((X - centroids[:, np.newaxis]) ** 2).sum(axis=2))
        
        # Step 3: Assign clusters (labels)
        labels = np.argmin(distances, axis=0)

        # Step 4: Compute new centroids
        new_centroids = np.array([X[labels == j].mean(axis=0) for j in range(k)])

        # Step 5: Check for convergence
        if np.allclose(centroids, new_centroids):
            break

        centroids = new_centroids

    # Step 6: Compute inertia (sum of squared distances to closest centroid)
    inertia = 0
    for j in range(k):
        inertia += np.sum((X[labels == j] - centroids[j]) ** 2)

    return centroids, labels, inertia
