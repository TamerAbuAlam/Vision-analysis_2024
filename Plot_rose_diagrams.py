# -*- coding: utf-8 -*-
"""
Detailed description of the code is provided below the "README" section. This code is part of a series of scripts designed to analyze text from national and international visions. The current script visualizes data as a rose diagram. This script represents step 2 out of 5 steps in the project. This project is known internally as "Ocean Visions".

Last updated: Fri, May 18, 2024, 14:25

Status: The script is working fine.

Author: Tamer Abu-Alam (tamer.abu-alam@uit.no)
"""

import pandas as pd ## in this case used to extract data from excel file
import plotly.io as io ##plotting 
import plotly.graph_objects as go
import plotly.express as px
io.renderers.default='browser' ## plot in browser 


df = pd.read_excel('Rose_diagram_cluster4.xlsx') ## creates a dataframe from the excel file

fig = px.bar_polar(df, r="Number of Visions", theta="Angel",
                   color="Factor", labels=("Factor"), template="plotly_white",
                   color_discrete_sequence= px.colors.sequential.Plasma_r)
fig.show()


"""
README for Rose Diagram Visualization Code
Overview

This script visualizes data from an Excel file as a rose diagram using Plotly. It reads the data into a pandas DataFrame and creates an interactive polar bar chart to illustrate the number of visions per angel, categorized by a specific factor.
Dependencies

Ensure you have the following Python libraries installed:

    pandas
    plotly

You can install them using pip commands.
Code Description
Imports

The script begins by importing essential libraries for data manipulation and visualization:

    pandas: Used for reading data from an Excel file and manipulating it into a suitable format.
    plotly: Utilized for creating interactive plots. The script sets Plotly's default renderer to display plots in a web browser for an interactive experience.

Data Loading

The script loads data from an Excel file named Rose_diagram_cluster4.xlsx into a pandas DataFrame. This DataFrame serves as the main structure for holding and manipulating the data before visualization. The Excel file should be located in the same directory as the script to ensure proper loading.
Data Visualization

A polar bar chart is created using Plotly Express:

    Data Mapping: The chart maps the number of visions to the radial distance and the angels to the angular coordinate.
    Categorization: Data is categorized by a factor, with different colors representing different factors to enhance visual distinction.
    Styling: The plot uses a sequential color scheme for aesthetic appeal and a white template for a clean look.

Usage

    Prepare the Data: Ensure your data is in an Excel file named Rose_diagram_cluster4.xlsx, formatted with columns for the number of visions, angels, and a categorizing factor.
    Run the Script: Execute the script in a Python environment.
    View the Plot: The resulting plot will open in your default web browser, displaying an interactive polar bar chart.

Notes

    Verify that the Excel file contains the necessary columns: "Number of Visions", "Angel", and "Factor".
    Customize plot parameters as needed to fit specific data and visualization requirements.
    Ensure all dependencies are correctly installed and configured to avoid errors during execution.
"""