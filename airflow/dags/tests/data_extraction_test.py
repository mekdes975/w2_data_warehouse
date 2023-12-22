import unittest
from unittest.mock import MagicMock
from src.extract_data_source import get_data  # Import the get_data class from your script
import pandas as pd 

class TestDataExtraction(unittest.TestCase):
    def setUp(self):
        self.data_obj = get_data()

    def test_get_data1(self):
        # Mocking the pd.read_csv method
        pd.read_csv = MagicMock(return_value=pd.DataFrame({
            'Col1': [1, 2, 3],
            'Col2': [4, 5, 6],
            'Col3': [7, 8, 9],
            'Col4': [10, 11, 12],
            'Col5': [13, 14, 15],
            'Col6': [16, 17, 18],
            'Col7': [19, 20, 21],
        }))
        
        expected_result = pd.DataFrame({
            'Col1': [1, 2, 3],
            'Col2': [4, 5, 6],
            'Col3': [7, 8, 9],
            'Col4': [10, 11, 12],
        })
        result = self.data_obj.get_data1()
        pd.read_csv.assert_called_once()  # Check if pd.read_csv was called
        self.assertTrue(result.equals(expected_result))  # Check if the result matches the expected data

    def test_get_data2(self):
        # Mocking the pd.read_csv method
        pd.read_csv = MagicMock(return_value=pd.DataFrame({
            'Col1': [1, 2, 3],
            'Col2': [4, 5, 6],
            'Col3': [7, 8, 9],
            'Col4': [10, 11, 12],
            'Col5': [13, 14, 15],
            'Col6': [16, 17, 18],
            'Col7': [19, 20, 21],
        }))
        
        expected_result = pd.DataFrame({
            'Col5': [13, 14, 15],
            'Col6': [16, 17, 18],
            'Col7': [19, 20, 21],
        })
        result = self.data_obj.get_data2()
        pd.read_csv.assert_called_once()  # Check if pd.read_csv was called
        self.assertTrue(result.equals(expected_result))  # Check if the result matches the expected data

if __name__ == '__main__':
    unittest.main()
