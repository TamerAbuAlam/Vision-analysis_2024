# -*- coding: utf-8 -*-
"""
Detailed description of the code is provided below the "README" section. This code is part of a series of scripts designed to analyze text from national and international visions. The current script utilizes the Hugging Face Transformers library to summarize text from a given input file. This script represents step 5 out of 5 steps in the project. This project is known internally as "Ocean Visions".

Last updated: Fri, May 18, 2024, 14:25

Status: The script is working fine.

Author: Tamer Abu-Alam (tamer.abu-alam@uit.no)
"""

from transformers import pipeline

# Function to summarize text
def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Main function to read text file and summarize it
def summarize_text_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    summary = summarize_text(text)
    
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(summary)
    
    return summary

# Summarize the text file and save the result
input_file_path = 'C:/Users/tab009/OneDrive - UiT Office 365/Tamer home/Research/Proposals/Ocean vision/New data and codes 26042024/topic modelling/cluster1/input_text.txt'  # Replace with your text file path
output_file_path = 'summary_output.txt'  # Replace with your desired output file path

summary = summarize_text_file(input_file_path, output_file_path)
print("Summary saved to:", output_file_path)
print("Summary:", summary)

"""
README for Text Summarization Script
Overview

This script utilizes the Hugging Face Transformers library to summarize text from a given input file. It reads the text from the specified file, generates a summary, and saves the summary to an output file.
Dependencies

Ensure you have the following Python library installed:

    transformers

You can install it using the appropriate package manager.
Code Description
Imports

The script imports necessary functions from the Hugging Face Transformers library to create a text summarization pipeline.
Text Summarization Function

The script defines a function to summarize text, which:

    Initializes a summarization pipeline.
    Generates a summary of the provided text, specifying constraints on the summary length.
    Returns the summarized text.

Main Function

The main function handles reading from and writing to files:

    Reads the content of the input text file specified by the user.
    Calls the text summarization function to generate a summary.
    Writes the summary to an output text file specified by the user.
    Returns the summary for display or further use.

Usage

    Prepare the Text File: Ensure your input text file is located at the specified path.
    Run the Script: Execute the script in a Python environment. Modify the input and output file paths to match your file locations.
    View the Summary: The script will save the generated summary to the specified output file and print the summary and output file path to the console.

Example

To summarize a text file located at a specific path and save the summary to an output file, modify the input and output file path variables accordingly. Run the script to generate and save the summary.
Notes

    Ensure the input text file contains plain text data.
    Adjust the parameters in the text summarization function as needed to customize the summary length.
    Ensure the Transformers library is correctly installed and configured to avoid errors during execution.
"""
