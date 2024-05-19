"""
Detailed description of the code is provided below the "Code Description" section.
This code is part of a series of scripts designed to analyze text from national and international visions.
The current script is intended to cluster the different visions.
This script represents step 1 out of 5 steps in the project.
This project is known internally as "Ocean Visions".

Last updated: Fri, May 18, 2024, 14:25

Status: The script is working fine.

Author: Tamer Abu-Alam (tamer.abu-alam@uit.no)

"""

import pandas as pd ## in this case used to extract data from excel file
import plotly.io as io ##plotting 
io.renderers.default='browser' ## plot in browser 
from sklearn.cluster import KMeans ## sklearn - a module for ML (neuron network, random forest ...) - we import only KMeans 
from sklearn.preprocessing import MinMaxScaler ## preprosess data scales
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

df = pd.read_excel('Data.xlsx') ## creates a dataframe from the excel file

X=df.drop("ID",axis=1)
#scaler = MinMaxScaler()
#scaler.fit(X)
#X=scaler.transform(X)
#X=X[:180] ## use it to find where the error is

# use this to see intertia
inertia = []
for i in range(1,12):
    kmeans = KMeans(
        n_clusters=i, init="k-means++",
        n_init=10,
        tol=1e-04, random_state=42
    )
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

fig = go.Figure(data=go.Scatter(x=np.arange(1,12),y=inertia))
fig.update_layout(title="Inertia vs Cluster Number",xaxis=dict(range=[0,11],title="Cluster Number"),
                  yaxis={'title':'Inertia'})
fig.show()

## use for clustering grapth - n_clusters is the number of clusters 
kmeans = KMeans(
        n_clusters=4 , init="k-means++",
        n_init=10,
        tol=1e-04, random_state=42
    )
kmeans.fit(X)

clusters=pd.DataFrame(X,columns=df.drop("ID",axis=1).columns)
clusters['label']=kmeans.labels_
polar=clusters.groupby("label").mean().reset_index()
polar=pd.melt(polar,id_vars=["label"])
fig4 = px.line_polar(polar, r="value", theta="variable", color="label", line_close=True,height=800,width=1400)
fig4.show()

df['cluster']=kmeans.labels_

# Save the dataframe with cluster labels to a CSV file
df.to_csv('Clustered_data.csv', index=False)


""" Code Description
Imports

The script begins by importing the necessary libraries for data manipulation, clustering, and visualization. pandas is used for data handling, plotly for creating interactive plots, sklearn for machine learning algorithms, and numpy for numerical operations.
Data Loading

The data is loaded from an Excel file named Data.xlsx into a pandas DataFrame. This file should be in the same directory as the script.
Data Preparation

The script drops the "ID" column from the DataFrame as it is not needed for clustering. The remaining data is stored in a variable for further processing.
(Optional) Data Scaling

There is commented-out code for scaling the data using MinMaxScaler from sklearn. This section can be uncommented if data scaling is necessary for your analysis.
Clustering and Inertia Calculation

To determine the optimal number of clusters, the script calculates the inertia for different numbers of clusters (from 1 to 11). Inertia measures how tightly the clusters are formed, which helps in deciding the appropriate number of clusters.
Inertia Visualization

The inertia values for different cluster numbers are visualized using Plotly. This plot helps in identifying the "elbow point," where adding more clusters doesn't significantly reduce inertia, indicating the optimal number of clusters.
Clustering

The script then performs KMeans clustering with a specified number of clusters (in this case, 4). The clustering model is fitted to the data, and cluster labels are assigned to each data point.
Cluster Visualization

A polar plot is created to visualize the characteristics of each cluster. The average values of each feature for each cluster are plotted, giving a clear picture of the cluster profiles.
Saving Results

Finally, the script adds the cluster labels to the original DataFrame and saves the resulting DataFrame to a CSV file named Clustered_data.csv.
Usage

    Ensure your data is in an Excel file named Data.xlsx and located in the same directory as the script.
    Run the script.
    View the interactive plots in your browser.
    Check the Clustered_data.csv file for the data with cluster labels.

Notes

    Adjust the number of clusters in the KMeans initialization as needed.
    Uncomment the scaling section if your data requires normalization.
    Ensure all dependencies are installed and properly configured.



"""