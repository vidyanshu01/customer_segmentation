from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

def train_kmeans(data, n_clusters=4):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(data)
    return kmeans, clusters

def visualize_clusters(data, clusters):
    plt.figure(figsize=(8,6))
    sns.scatterplot(x=data[:,0], y=data[:,1], hue=clusters, palette='viridis')
    plt.title("Customer Segmentation using K-Means")
    plt.show()
