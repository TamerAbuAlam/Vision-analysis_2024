# -*- coding: utf-8 -*-
"""
Detailed description of the code is provided below the "README" section. This code is part of a series of scripts designed to analyze text from national and international visions. The current script performs KMeans clustering, reduces dimensionality using PCA, and visualizes the results. This script represents step 3 out of 5 steps in the project. This project is known internally as "Ocean Visions".

Last updated: Fri, May 18, 2024, 14:25

Status: The script is working fine.

Author: Tamer Abu-Alam (tamer.abu-alam@uit.no)
"""
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

# Read the input data from the Excel file
df = pd.read_excel('Input_data_for_clustring.xlsx')

# Extract the features for clustering (excluding 'ID')
X = df.drop("ID", axis=1)

# Perform KMeans clustering
kmeans = KMeans(n_clusters=4, init="k-means++", n_init=10, tol=1e-04, random_state=42)
kmeans.fit(X)

# Add cluster labels to the dataframe
df['cluster'] = kmeans.labels_

# Dimensionality Reduction with PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
df_pca = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
df_pca['cluster'] = df['cluster'].astype(int)  # Ensure cluster labels are integers
df_pca['ID'] = df['ID']  # Include ID for hover information

# Create the scatter plot for clusters
fig = px.scatter(df_pca, x='PC1', y='PC2', color=df_pca['cluster'].astype(str),
                 labels={'color': 'Cluster'}, hover_data=['ID'])

# Plotting centroids
centers_pca = pca.transform(kmeans.cluster_centers_)
centers_df = pd.DataFrame(data=centers_pca, columns=['PC1', 'PC2'])
centers_df['cluster'] = ['Centroid'] * len(centers_df)

# Adding centroids to the plot
for i, row in centers_df.iterrows():
    fig.add_trace(go.Scatter(x=[row['PC1']], y=[row['PC2']],
                             mode='markers+text',
                             marker_symbol='star',
                             marker_size=15,
                             marker_color='yellow',
                             text='Centroid',
                             textposition='top center'))

fig.update_layout(title='Visualization of Visions with Cluster Centroids',
                  xaxis_title='Principal Component 1',
                  yaxis_title='Principal Component 2',
                  legend_title='Cluster')

# Calculate distance from each point to its cluster centroid
df_pca['distance_to_centroid'] = df_pca.apply(
    lambda row: np.linalg.norm(centers_pca[int(row['cluster'])] - np.array([row['PC1'], row['PC2']])), axis=1)

# Save detailed data to CSV
df_detailed = df_pca[['ID', 'cluster', 'PC1', 'PC2', 'distance_to_centroid']]
df_detailed.to_csv('Detailed_cluster_data.csv', index=False)

# Save to HTML
fig.write_html('cluster_visualization.html')

# Show the plot
fig.show()

"""
README for Clustering and PCA Visualization Code
Overview

This script performs KMeans clustering on a dataset, reduces the dimensionality using PCA, and visualizes the results using Plotly. It includes the identification of cluster centroids and computes the distance of each point from its respective cluster centroid.
Dependencies

Ensure you have the following Python libraries installed:

    pandas
    scikit-learn
    plotly
    numpy

You can install them using pip commands.
Code Description
Imports

The script begins by importing essential libraries for data manipulation, clustering, dimensionality reduction, and visualization:

    pandas: Used for reading data from an Excel file and manipulating it into a suitable format.
    scikit-learn: Utilized for performing KMeans clustering and PCA for dimensionality reduction.
    plotly: Used for creating interactive plots and visualizations.
    numpy: Used for numerical operations and distance calculations.

Data Loading

The script loads data from an Excel file named Input_data_for_clustring.xlsx into a pandas DataFrame. This DataFrame serves as the main structure for holding and manipulating the data before clustering and visualization. The Excel file should be located in the same directory as the script.
Data Preparation

The script extracts the features for clustering by dropping the "ID" column from the DataFrame. This prepares the data for the clustering algorithm.
Clustering

The script performs KMeans clustering on the dataset, specifying the number of clusters and other parameters. Cluster labels are assigned to each data point and added to the DataFrame.
Dimensionality Reduction

The script uses PCA to reduce the data to two principal components. This reduced data is then stored in a new DataFrame, which also includes the cluster labels and IDs for reference.
Visualization

A scatter plot is created using Plotly Express to visualize the clusters in the reduced two-dimensional space. Different colors represent different clusters, and IDs are included for hover information.
Plotting Centroids

The centroids of the clusters are transformed using PCA and added to the scatter plot as star-shaped markers. This helps in visualizing the central points of each cluster.
Distance Calculation

The script calculates the distance of each point from its cluster centroid. This information is added to the DataFrame for detailed analysis.
Saving Results

The script saves the detailed data, including the distances to centroids, to a CSV file named Detailed_cluster_data.csv. Additionally, the interactive plot is saved as an HTML file named cluster_visualization.html.
Usage

    Ensure your data is in an Excel file named Input_data_for_clustring.xlsx and located in the same directory as the script.
    Run the script.
    View the interactive plot in your browser and the detailed data in the Detailed_cluster_data.csv file.

Notes

    Verify that the Excel file contains the necessary columns, excluding "ID" for clustering features.
    Adjust the number of clusters and other parameters in the KMeans algorithm as needed.
    Customize plot parameters and labels to fit specific data and visualization requirements.
    Ensure all dependencies are correctly installed and configured to avoid errors during execution.


"""