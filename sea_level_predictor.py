import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # ------------------------------------------------------------------
    # Question 1:
    # Use matplotlib to create a scatter plot using the Year column as
    # the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
    # ------------------------------------------------------------------
    fig, ax = plt.subplots()

    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax.set_xlabel('Year')
    ax.set_ylabel('CSIRO Adjusted Sea Level')
    ax.set_title('Rise in Sea Level')

    # ------------------------------------------------------------------
    # Question 2:
    # Use the linregress function from scipy.stats to get the slope and
    # y-intercept of the line of best fit.
    # Plot the line of best fit over the top of the scatter plot.
    # Make the line go through the year 2050 to predict the sea level
    # rise in 2050.
    # ------------------------------------------------------------------

    result = linregress(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    x_pred = np.arange(df['Year'].min(), 2051)

    y_pred = result.slope * x_pred + result.intercept

    ax.plot(x_pred, y_pred, color='red')

    # ------------------------------------------------------------------
    # Question 3:
    # Plot a new line of best fit using only data from year 2000 onward.
    # Extend the line through the year 2050 to predict future sea level.
    # ------------------------------------------------------------------

    df_2000 = df[df['Year'] >= 2000]

    result_2000 = linregress(
        df_2000['Year'],
        df_2000['CSIRO Adjusted Sea Level']
    )

    x_pred_2000 = np.arange(2000, 2051)

    y_pred_2000 = (
        result_2000.slope * x_pred_2000
        + result_2000.intercept
    )

    ax.plot(x_pred_2000, y_pred_2000, color='green')

    # ------------------------------------------------------------------
    # Question 4:
    # Set title and axis labels.
    # ------------------------------------------------------------------

    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    plt.savefig('sea_level_plot.png')
    return plt.gca()    