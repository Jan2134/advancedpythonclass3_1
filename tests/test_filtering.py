"""
Script to test the filtering
"""

from scripts.script import FilterMovies
import unittest
import pandas as pd

class TestFilterMovies(unittest.TestCase):
    """
    Class to test filter for movie data
    """

    def setUp(self):
        """
        Create a sample DataFrame for testing
        """
        data = {
            "Title": ["Movie1", "Movie2", "Movie3"],
            "Genre": ["Action", "Comedy", "Drama"],
            "Inflation-Adjusted Gross": [100000000, 80000000, 120000000]
        }
        self.sample_df = pd.DataFrame(data)
        self.filter_movies_instance = FilterMovies(self.sample_df)

    def test_filter_by_genre(self):
        """
        Test filtering by genre
        """
        filtered_df = self.filter_movies_instance.filter_by_genre("Comedy")
        expected_df = pd.DataFrame({"Title": ["Movie2"], "Genre": ["Comedy"], "Inflation-Adjusted Gross": [80000000]})
        filtered_df.reset_index(drop=True, inplace=True)
        expected_df.reset_index(drop=True, inplace=True)

        pd.testing.assert_frame_equal(filtered_df, expected_df, check_like=True)

    def test_filter_by_bigger_gross(self):
        """
        Test filtering by bigger gross
        """
        filtered_df = self.filter_movies_instance.filter_by_bigger_gross(90000000)
        expected_df = pd.DataFrame({"Title": ["Movie1", "Movie3"], "Genre": ["Action", "Drama"], "Inflation-Adjusted Gross": [100000000, 120000000]})
        filtered_df.reset_index(drop=True, inplace=True)
        expected_df.reset_index(drop=True, inplace=True)

        pd.testing.assert_frame_equal(filtered_df, expected_df, check_like=True)

if __name__ == '__main__':
    unittest.main()
