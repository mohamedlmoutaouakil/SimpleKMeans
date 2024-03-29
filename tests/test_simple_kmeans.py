import sys
sys.path.append('..')

from simplekmeans.simple_kmeans import SimpleKMeans
import numpy as np
import unittest

class TestSimpleKMeans(unittest.TestCase):
    
    def test_init_random_centroids(self):
        n_clusters = 2
        skmeans = SimpleKMeans(k=n_clusters)
        X = np.array([[1, 2], [3, 4]])
        random_centroids = skmeans.init_random_centroids(X)
        self.assertEqual(np.array(random_centroids).shape, (n_clusters,2))
        
    def test_init_clusters(self):
        n_clusters = 2
        skmeans = SimpleKMeans(k=n_clusters)
        clusters = skmeans.init_clusters()
        self.assertEqual(len(clusters), n_clusters)
        for cluster_index in range(n_clusters):
            self.assertEqual(clusters[cluster_index], [])
            
    def test_nearest_centroid(self):
        n_clusters = 2
        skmeans = SimpleKMeans(k=n_clusters)
        skmeans.centroids = [np.array([1,1]), np.array([4,4])]
        x1 = np.array([2, 2])
        x2 = np.array([3, 3])
        x1_nearest_centr = skmeans.nearest_centroid(x1)
        x2_nearest_centr = skmeans.nearest_centroid(x2)
        self.assertEqual(x1_nearest_centr, 0)
        self.assertEqual(x2_nearest_centr, 1)
        
    def test_cluster_points(self):
        n_clusters = 2
        skmeans = SimpleKMeans(k=n_clusters)
        skmeans.centroids = [np.array([1,1]), np.array([4,4])]
        X = np.array([[2,2], [1.5, 2], [3, 3], [3.5, 3]])
        expected_clusters = {0: [[2, 2], [1.5, 2]],
                             1: [[3, 3], [3.5, 3]]}
        clusters = skmeans.cluster_points(X)
        for cluster_index in range(n_clusters):
            cluster_tolist = [point.tolist() for point in clusters[cluster_index]]
            self.assertListEqual(cluster_tolist, expected_clusters[cluster_index])
            
    def test_calculate_new_centroids(self):
        n_clusters = 2
        skmeans = SimpleKMeans(k=n_clusters)
        clusters = {0: [np.array([1, 2]), np.array([3, 4])],
                    1: [np.array([5.5, 3.2]), np.array([7, 9.8])]}
        centroids = skmeans.calculate_new_centroids(clusters, 2)
        expected_centroids = [[2.0, 3.0], [6.25, 6.5]]
        self.assertCountEqual(centroids.tolist(), expected_centroids)
        
    def test_fit(self):
        X = np.array([[2,2], [1.5, 2], [3, 3], [3.5, 3]])
        skmeans = SimpleKMeans()
        skmeans.fit(X)
        centroids = skmeans.centroids
        expected_centroids = [[1.75, 2.0], [3.25, 3.0]]
        self.assertCountEqual(centroids.tolist(), expected_centroids)
        
    def test_predict(self):
        X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
        skmeans = SimpleKMeans()
        skmeans.fit(X)
        expected_centroids = [0, 1, 0, 1, 1]
        predicted_centroids = skmeans.predict([[0, 0], [6, 3], [-1.1, -5], [12, 3], [20, 80]])
        self.assertCountEqual(predicted_centroids, expected_centroids)
        
if __name__ == '__main__':
    unittest.main()