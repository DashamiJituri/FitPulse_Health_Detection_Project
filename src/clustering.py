from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
import pandas as pd

def run_kmeans(features, k=3):
    model = KMeans(n_clusters=k, random_state=42)
    return model.fit_predict(features)

def run_dbscan(features):
    model = DBSCAN(eps=0.5, min_samples=5)
    return model.fit_predict(features)

def apply_pca(features):
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(features)
    return pd.DataFrame(reduced, columns=["PC1", "PC2"])
