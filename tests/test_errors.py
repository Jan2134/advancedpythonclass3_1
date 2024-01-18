"""
Test plotting of the dataset
"""
import unittest
import pandas as pd
from unittest.mock import patch # found on the internet
from scripts.script import plot_data

class TestPlotting(unittest.TestCase):

    def setUp(self):
        """
        Create a sample DataFrame for testing
        """
        data = {
            "x_data": [1, 2, 3],
            "y_data": [4, 5, 6],
        }
        self.sample_df = pd.DataFrame(data)

    @patch('builtins.print')
    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.plot')
    def test_plotting_successful(self, mock_plot, mock_show, mock_print):
        """
        Test successful plotting
        """
        with patch('matplotlib.pyplot.xlabel'), patch('matplotlib.pyplot.ylabel'), patch('matplotlib.pyplot.title'):
            plot_data(self.sample_df, "x_data", "y_data")

        mock_plot.assert_called_once_with(self.sample_df["x_data"], self.sample_df["y_data"])
        mock_show.assert_called_once()

        mock_print.assert_not_called()

if __name__ == '__main__':
    unittest.main()
