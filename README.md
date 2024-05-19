# Vision-analysis_2024

Before using the attached script files, read this "READ ME" file.

The Project

This project includes several Python scripts that aim to analyze, classify, cluster, and perform topic modeling analysis for vision texts. The visions are collected from national and international resources as part of a project/report supported by IPBES (Intergovernmental Science-Policy Platform on Biodiversity and Ecosystem Services).

Author: The scripts were written by Dr. Tamer Abu-Alam (tamer.abu-alam@uit.no) - UiT The Arctic University of Norway

Last update: 19 May 2024

Language: Python 3.11 - written in Spyder

File formats: The scripts are .py files. The scripts read and write files of different formats such as Excel, CSV, TXT, and HTML.

Each script uses some Python packages and libraries. Each script has a "Read Me" section to define the action of the script, the files that the script reads and writes, and the different packages/libraries used by the script.

These scripts can be distributed under Creative Commons licenses: CC BY-NC-ND

An updated version of the scripts can be downloaded here: https://github.com/TamerAbuAlam/Vision-analysis_2024
 
The following are the different steps and the different scripts included:
-------------------------------------------------
Step 1: Clustering using K Means Method

Script file: Clustering_K_means.py
Libraries used: pandas, plotly.io, sklearn.cluster, sklearn.preprocessing, plotly, numpy

Action:
This script uses the Elbow method to define how many clusters exist in the database. Then, the script clusters the different visions using the K Means method. The output data/clusters are saved in "Clustered_data.csv". The script also presents the results as different figures.

Last updated: Fri, May 18, 2024, 14:25

------------------------------------------------
Step 2: Visualize the Different Clusters

Script file: Plot_rose_diagrams.py
Libraries used: pandas, plotly.io, plotly.graph_objects, plotly.express

Action:
This script visualizes data from an Excel file as a rose diagram using Plotly. It reads the data into a pandas DataFrame and creates an interactive polar bar chart to illustrate the number of visions per angel, categorized by a specific factor.

------------------------------------------------
Step 3: Score the Different Visions

Script file: score_the_visions.py
Libraries used: pandas, sklearn.cluster, sklearn.decomposition, plotly.express, numpy, plotly.graph_objects

Action:
This script performs KMeans clustering on a dataset, reduces the dimensionality using PCA, and visualizes the results using Plotly. It includes the identification of cluster centroids and computes the distance of each point from its respective cluster centroid.

------------------------------------------------
Step 4: Topic Modeling

Script file: Topic_modeling_5_top_topics_and_the_most_10_words.py
Libraries used: nltk, gensim, numpy, pandas

Action:
This script is designed for text preprocessing, topic modeling, and word frequency analysis. It utilizes the Natural Language Toolkit (nltk) and gensim libraries to process and analyze text data. The script performs tasks such as cleaning and tokenizing the text, removing stop words, identifying key topics using Latent Dirichlet Allocation (LDA), and counting the most frequently occurring words.

------------------------------------------------
Step 5: Text Summarization

Script file: Text_summarization.py
Libraries used: transformers

Action:
This script utilizes the Hugging Face Transformers library to summarize text from a given input file. It reads the text from the specified file, generates a summary, and saves the summary to an output file.
