import matplotlib.pyplot as plt
import pandas as pd
import datetime

def plot_time_series(data, x_col, y_cols, colors, title,
                     x_axis, y_axis, filename="result.png"):
    """
    Plot time series data with multiple series on the Y-axis.

    @param data: dictionary containing time series data.
    # Sample data with datetime objects for the 'Time' column
    data = {
        'Time': [datetime(2024, 2, 1), datetime(2024, 2, 2), datetime(2024, 2, 3), datetime(2024, 2, 4), datetime(2024, 2, 5)],
        'Series1': [10, 15, 12, 18, 20],
        'Series2': [8, 13, 10, 16, 18],
        'Series3': [5, 8, 6, 10, 12]
    }
    @param x_col Column name for the X-axis (time).
    @param y_col List of column names for the Y-axis (series values).
    @param colors List of colors for each series.
    @param title Chart title
    @param x_axis Title of the X Axis
    @param y_axis Title of the Y Axis

    @return None 

    Sideeffect:
    Plots time series data and saves it in the file
    """
    df = pd.DataFrame(data)
    # Plotting
    plt.figure(figsize=(10, 6))

    for y_col, color in zip(y_cols, colors):
        plt.plot(df[x_col].values, df[y_col].values, label=y_col, marker='o', color=color)

    # Formatting the plot
    plt.title(title)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

    # Save the plot in the provided file
    plt.savefig(filename, bbox_inches='tight')

def main():

    # Colors for each series
    series_colors = ['blue', 'orange']

    """
    data = {
        'Time': [datetime(2024, 2, 1), datetime(2024, 2, 2), datetime(2024, 2, 3), datetime(2024, 2, 4), datetime(2024, 2, 5)],
        'Series1': [10, 15, 12, 18, 20],
        'Series2': [8, 13, 10, 16, 18],
        'Series3': [5, 8, 6, 10, 12]
    }
    """
    data = {'Time': (datetime.datetime(2024, 2, 4, 0, 9, 31, 325578),), 'togetherai': (0.28866517599999497,), 'anyscale': (0.8054724669991629,)}

    # Plotting using the routine
    plot_time_series(data, 'Time', ['togetherai', 'anyscale'], series_colors, "Time Series Chart", "Time", "Values")


if __name__ == "__main__":
    main()
