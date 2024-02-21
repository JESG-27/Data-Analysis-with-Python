import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    first_line = pd.Series(int(i) for i in range(1880, 2051))
    first_regress = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(first_line, first_regress.intercept + first_regress.slope * first_line, color='red')

    # Create second line of best fit
    df = df[df['Year'] >= 2000]
    second_line = pd.Series(int(i) for i in range(2000, 2051))
    second_regress = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(second_line, second_regress.intercept + second_regress.slope * second_line, color='orange')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()