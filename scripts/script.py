"""
Filter through Movie Dataset
"""

import pandas as pd
import click
import matplotlib.pyplot as plt

class FilterMovies:
    """
    Class to filter the movie ratings
    """
    def __init__(self, df):
        self.df = df
        
    def filter_by_genre(self, genre):
        return self.df[self.df["Genre"]==genre]

    def filter_by_bigger_gross(self, gross):
        return self.df[self.df["Inflation-Adjusted Gross"] > gross]


@click.command(short_help="Filter through Movie Dataset")
@click.option("-id", "--input_data", required=True, help="Input the data set")
@click.option("-f", "--filtering", is_flag=True, help="Tackle to initialize filtering")
@click.option("-p1", "--plt_1", help="Plotting argument 1")
@click.option("-p2", "--plt_2", help="Plotting argument 2")
@click.option("-ge", "--genre", help="Filter movies by genre")
@click.option("-gr", "--gross", help="Filter movies by bigger gross")

def main(input_data, filtering, plt_1, plt_2, genre, gross):
    """
    Main execution function
    """
    df = pd.read_csv(input_data)
    print(f"This is my input data {input_data}:")
    print(df.head())
    print("\n")

    if filtering:
        filter_description = f"I am filtering for"
        if genre:
            print(filter_description + f" genre {genre}:")
            df = FilterMovies(df).filter_by_genre(genre)
        if gross:
            print(filter_description + f" gross bigger than {gross}:")
            df = FilterMovies(df).filter_by_bigger_gross(int(gross))
        print(df.head())
        
    # worked with Years (-p1 Year) over Gross (-p2 Gross)
    if plt_1 and plt_2:
        try:
            df[plt_1] = pd.to_numeric(df[plt_1], errors='coerce')
            df[plt_2] = pd.to_numeric(df[plt_2], errors='coerce')

            plt.plot(df[plt_1], df[plt_2])
            plt.xlabel(plt_1)
            plt.ylabel(plt_2)
            plt.title(f"{plt_2} over {plt_1}")
            plt.show()
        except Exception as e:
            print(f"Error plotting: {e}")

if __name__ == "__main__":
    main()