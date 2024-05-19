# -*- coding: utf-8 -*-
"""
Detailed description of the code is provided below the "README" section. This code is part of a series of scripts designed to analyze text from national and international visions. The current script is designed for text preprocessing, topic modeling, and word frequency analysis. This script represents step 4 out of 5 steps in the project. This project is known internally as "Ocean Visions".

Last updated: Fri, May 18, 2024, 14:25

Status: The script is working fine.

Author: Tamer Abu-Alam (tamer.abu-alam@uit.no)
"""
import nltk
import gensim
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim import corpora, models
from collections import Counter
import pandas as pd

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Function to preprocess the text
def preprocess(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return filtered_tokens

# Function to perform topic modeling
def extract_topics(text, num_topics=5, num_words=20):
    tokens = preprocess(text)
    dictionary = corpora.Dictionary([tokens])
    corpus = [dictionary.doc2bow(tokens)]
    lda_model = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)
    topics = lda_model.print_topics(num_words=num_words)
    topic_words = {}
    for i, topic in enumerate(topics):
        words = topic[1].split(' + ')
        words = [word.split('*')[1].replace('"', '').strip() for word in words]
        topic_words[f'Topic {i+1}'] = words
    return topic_words

# Function to extract top N words
def extract_top_words(text, top_n=10):
    tokens = preprocess(text)
    word_freq = Counter(tokens)
    top_words = word_freq.most_common(top_n)
    return top_words

# Function to save results to CSV
def save_to_csv(topic_words, top_words, output_file='analysis_results.csv'):
    # Convert topic words to a DataFrame
    topic_df = pd.DataFrame.from_dict(topic_words, orient='index').transpose()
    
    # Prepare top words data for DataFrame
    top_words_df = pd.DataFrame(top_words, columns=['Word', 'Frequency'])
    
    # Save the DataFrames to a CSV file with different sections
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('Topics\n')
        topic_df.to_csv(file, index=False)
        file.write('\nTop Words\n')
        top_words_df.to_csv(file, index=False)

# Main function to analyze text file
def analyze_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    topic_words = extract_topics(text)
    top_words = extract_top_words(text)
    save_to_csv(topic_words, top_words)

# Analyze the text file
file_path = 'C:/Users/tab009/OneDrive - UiT Office 365/Tamer home/Research/Proposals/Ocean vision/New data and codes 26042024/topic modelling/cluster1/input_text.txt'  # Replace with your text file path
analyze_text_file(file_path)

"""
READ ME
-------
This Python script is designed for text preprocessing, topic modeling, and word frequency analysis. It utilizes the Natural Language Toolkit (nltk) and gensim libraries to process and analyze text data. Below is a detailed description of the script's functionality.
Overview

The script performs the following tasks:

    Text Preprocessing: Cleans and tokenizes the text, removes stop words, and filters non-alphabetic characters.
    Topic Modeling: Uses Latent Dirichlet Allocation (LDA) to identify key topics in the text and extracts the most relevant words for each topic.
    Word Frequency Analysis: Counts and identifies the most frequently occurring words in the text.
    Save Results: Saves the results of the analysis (topics and top words) to a CSV file for further review.

Detailed Functionality
1. Text Preprocessing

The script preprocesses the text by:

    Converting it to lowercase.
    Tokenizing the text into individual words.
    Removing punctuation and non-alphabetic characters.
    Filtering out common stop words to focus on the most meaningful words.

2. Topic Modeling

The topic modeling process involves:

    Preprocessing the text to obtain tokens.
    Creating a dictionary and corpus required by the LDA model.
    Fitting the LDA model to the corpus to identify a specified number of topics.
    Extracting the top words associated with each identified topic.

3. Word Frequency Analysis

The script counts the frequency of each word in the preprocessed text and extracts the top N most frequent words.
4. Save Results to CSV

The script saves the analysis results into a CSV file, with separate sections for topics and top words. The CSV file is structured for easy review and further analysis.
Usage Instructions

    Ensure Necessary Libraries are Installed:
        Install nltk, gensim, numpy, and pandas if they are not already installed.
        Download the necessary NLTK data (punkt and stopwords).

    Prepare Your Text File:
        Place your text file in an accessible directory.
        Update the file_path variable in the script to point to your text file.

    Run the Script:
        Execute the script in your Python environment.
        The script will read the text file, perform the analysis, and save the results to analysis_results.csv.
"""